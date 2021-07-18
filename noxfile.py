from os import PathLike
from typing import Union

import nox

SOURCE: Union[str, PathLike[str]] = "./src/"
MISC: list[Union[str, PathLike[str]]] = ["./noxfile.py"]


@nox.session
def format_and_lint(session: nox.Session) -> None:
    session.install("flake8", "black", "mypy")

    session.run("black", SOURCE, *MISC)
    session.run("flake8", "--max-line-length", "88", SOURCE, *MISC)
    session.run("mypy", "--strict", "--python-version", "3.9", SOURCE)
