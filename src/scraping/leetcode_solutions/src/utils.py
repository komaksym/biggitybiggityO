import re
import subprocess


def set_regex_pattern(pattern, flags=0):
    return re.compile(rf"{pattern}", flags)


def search_files(folder_path):
    """Search files locally and parse them and their paths into python objects"""
    raw_data = {"file_paths": [], "files": []}

    for file_path in folder_path.glob("*.py"):
        raw_data["file_paths"].append(file_path)
        raw_data["files"].append(file_path.read_text())

    return raw_data


def open_corrupted_files(command, posix_paths, destination_path=None):
    # Subprocess command
    command = command
    paths = [command]

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
