from os import PathLike
from typing import Union

import nox

SOURCE: Union[str, PathLike] = "./src/"
MISC: list[Union[str, PathLike]] = ["./noxfile.py"]


@nox.session
def format_and_lint(session: nox.Session) -> None:
    session.install("flake8", "black", "mypy")

    session.run("black", SOURCE, *MISC)
    session.run("flake8", "--max-line-length", "88", SOURCE, *MISC)
    session.run("mypy", SOURCE)
