# simple-video-editor

CLI for basic video editing capabilities

## Dependencies

You will need `ffmpeg` on your system (and PATH). This is tested on mac and linux machines
and **should** work on windows where it was initially developed.

### Mac ffmpeg

`brew install ffmpeg`

It should be added to PATH and `moviepy` should pick it up, if it does not, you can always
set the env var `IMAGEIO_FFMPEG_EXE` to point to it

## Installation

It is recommended to just install the requirements from the `requirements.txt` file before
the package: `pip install .` . This is because there is an issue with `cutout` in `moviepy`
that was fixed on branch but not merged yet.
