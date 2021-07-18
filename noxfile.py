from os import PathLike
from typing import Union

import nox

SOURCE: Union[str, PathLike[str]] = "./src/"
MISC: list[Union[str, PathLike[str]]] = ["./noxfile.py"]


@nox.session
def black_format(session: nox.Session) -> None:
    session.install("black")
    session.run("black", SOURCE, *MISC)


@nox.session
def lint(session: nox.Session) -> None:
    session.install("flake8")
    session.run("flake8", "--max-line-length", "88", SOURCE, *MISC)


@nox.session
def mypy(session: nox.Session) -> None:
    session.install("mypy")
    session.run("mypy", "--strict", "--python-version", "3.9", SOURCE)


@nox.session
def tests(session: nox.Session) -> None:
    session.install("pytest", ".")
    session.run("pytest")
