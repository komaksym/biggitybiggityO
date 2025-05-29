import re
import subprocess
from pathlib import Path
from typing import Any, TypedDict


class MyDict(TypedDict):
    file_paths: list[Path | str]
    files: list[str]


def set_regex_pattern(pattern: str, flags: Any = 0) -> re.Pattern[str]:
    return re.compile(rf"{pattern}", flags)


def search_files(folder_path: Path) -> MyDict:
    """Search files locally and parse them and their paths into python objects"""
    raw_data: MyDict = {"file_paths": [], "files": []}

    for file_path in folder_path.glob("*.py"):
        raw_data["file_paths"].append(file_path)
        raw_data["files"].append(file_path.read_text())

    return raw_data


def open_corrupted_files(
    command: str, posix_paths: list[Path | str], destination_path=None
) -> None:
    # Subprocess command
    paths: list[Any] = [command]

    # Populate the paths
    for p in posix_paths:
        # Get the str representation of PosixPath
        paths.append(str(p))

    # If moving files
    if command == "mv" and destination_path:
        paths.append(destination_path)

    # Run
    if posix_paths:
        subprocess.run(paths)
