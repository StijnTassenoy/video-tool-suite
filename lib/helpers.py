import os
import re
from typing import List

from rich import print as rprint


def clear_screen() -> None:
    """ Checks OS type and clears the console. """
    os.system("cls" if os.name == "nt" else "clear")


def get_all_videofiles_from_directory(working_directory: str, extensions: List[str]) -> List[str]:
    """ Gets all files from a given path wit certain extensions. """
    files = [f for f in os.listdir(working_directory)]  # if os.path.isfile(f)]
    for file in files:
        if not file.endswith(tuple(extensions)):
            files.remove(file)
    return files


def print_files_with_index(file_list: List[str]) -> None:
    print()
    for idx, file in enumerate(file_list):
        rprint(f"[bold blue][{str(idx+1)}][/bold blue] {file}")


def convert_to_timestamp(input_string: str) -> str:
    """ Convert string to hh:mm:ss format. """
    if input_string.endswith("s"):
        time_in_seconds = int(re.search(r"""(\d+)s""", input_string).group(1))
        hours, remainder = divmod(time_in_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    elif input_string.endswith("m"):
        time_in_minutes = int(re.search(r"""(\d+)m""", input_string).group(1))
        hours, minutes = divmod(time_in_minutes, 60)
        return f"{hours:02d}:{minutes:02d}:00"


def convert_timestamp_to_seconds(timestamp_string) -> str:
    """ Convert hh:mm:ss to seconds string. """
    hours, minutes, seconds = map(int, timestamp_string.split(":"))
    return f"{3600 * hours + 60 * minutes + seconds}s"
