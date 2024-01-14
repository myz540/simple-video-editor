from setuptools import find_packages, setup
import os


def find_scripts():
    scripts = os.listdir(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin")
    )
    script_paths = [os.path.join("bin", script) for script in scripts]
    return script_paths


def find_requirements():
    with open("requirements.txt") as fp:
        requirements = [line.strip().split("==")[0] for line in fp.readlines()]
    return requirements


setup(
    name="sve",
    version="0.1",
    description="Simple video editor CLI",
    author="Mike Zhong",
    packages=find_packages(),
    install_requires=find_requirements(),
    scripts=find_scripts(),
)
