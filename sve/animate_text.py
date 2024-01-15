import numpy as np
from typing import Callable, Tuple

from moviepy.editor import *
from moviepy.video.tools.segmenting import find_objects


# THE NEXT FOUR FUNCTIONS DEFINE FOUR WAYS OF MOVING THE LETTERS


# helper function
rotMatrix = lambda a: np.array([[np.cos(a), np.sin(a)], [-np.sin(a), np.cos(a)]])


def vortex(screenpos, i, nletters):
    d = lambda t: 1.0 / (0.3 + t**8)  # damping
    a = i * np.pi / nletters  # angle of the movement
    v = rotMatrix(a).dot([-1, 0])
    if i % 2:
        v[1] = -v[1]
    return lambda t: screenpos + 400 * d(t) * rotMatrix(0.5 * d(t) * a).dot(v)


def cascade(screenpos, i, nletters):
    v = np.array([0, -1])
    d = lambda t: 1 if t < 0 else abs(np.sinc(t) / (1 + t**4))
    return lambda t: screenpos + v * 400 * d(t - 0.15 * i)


def arrive(screenpos, i, nletters):
    v = np.array([-1, 0])
    d = lambda t: max(0, 3 - 3 * t)
    return lambda t: screenpos - 400 * v * d(t - 0.2 * i)


def vortexout(screenpos, i, nletters):
    d = lambda t: max(0, t)  # damping
    a = i * np.pi / nletters  # angle of the movement
    v = rotMatrix(a).dot([-1, 0])
    if i % 2:
        v[1] = -v[1]
    return lambda t: screenpos + 400 * d(t - 0.1 * i) * rotMatrix(-0.2 * d(t) * a).dot(
        v
    )


animations = {
    "arrive": arrive,
    "vortex": vortex,
    "vortexout": vortexout,
    "cascade": cascade,
}


def moveLetters(letters, funcpos):
    return [
        letter.set_pos(funcpos(letter.screenpos, i, len(letters)))
        for i, letter in enumerate(letters)
    ]


def make_clip(
    letters: str,
    funcpos: Callable,
    screensize: Tuple[int, int] = (720, 460),
    kerning: int = 5,
    fontsize: int = 100,
    color: str = "white",
    font: str = "Amiri-Bold",
) -> CompositeVideoClip:
    screensize = (720, 460)
    txtClip = TextClip(
        letters,
        color=color,
        font=font,
        kerning=kerning,
        #fontsize=fontsize,
    )
    cvc = CompositeVideoClip([txtClip.set_pos("center")], size=screensize)
    letters = find_objects(cvc)
    return CompositeVideoClip(moveLetters(letters, funcpos), size=screensize).subclip(
        0, 5
    )


def animate_text(text: str, animation: str, output_file: str = None):
    clip = make_clip(letters=text, funcpos=animations[animation])
    if output_file is None:
        output_file = f"{text}_animated_{animation}.mp4"
    clip.write_videofile(output_file)
