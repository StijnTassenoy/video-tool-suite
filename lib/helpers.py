# Python Imports #
import os
import re
from typing import List, Tuple, Optional

# External Module Imports #
from rich import print as rprint


def clear_screen() -> None:
    """ Checks OS type and clears the console. """
    os.system("cls" if os.name == "nt" else "clear")


def get_all_videofiles_from_directory(working_directory: str, extensions: Tuple) -> List[str]:
    """ Gets all files from a given path wit certain extensions. """
    files = []

    for file in os.listdir(working_directory):
        if file.endswith(extensions):
            files.append(file)
    return files


def print_files_with_index(file_list: List[str]) -> None:
    """ Print all files from a list with their 1-based index. """
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


def select_video_files(working_directory: str) -> Optional[List[str]]:
    """ Select valid input for video files from a directory. """
    video_files = get_all_videofiles_from_directory(working_directory, (".mp4", ".mkv"))
    if len(video_files) == 1:
        print_files_with_index(video_files)
        print()
        return video_files
    elif len(video_files) > 1:
        rprint("[bold blue][0][/bold blue] All files")
        print_files_with_index(video_files)
        choice = input("Make a choice or press enter to return: ")
        while True:
            try:
                if choice in ["back", "return", "no", ""]:
                    break
                if choice == "0":
                    return video_files
                elif int(choice) - 1 in range(len(video_files)) and not "":
                    return [video_files[int(choice) - 1]]
            except ValueError as ve:
                choice = input("Not an option. Make a valid choice or press enter to return: ")
    return None


def ask_start_and_end_time() -> Tuple[str, str]:
    """ Return a valid start and end time. """
    start_time = ask_for_time("Input the starting time of the clip: ")
    end_time = ask_for_time("Input the ending time of the clip: ")
    return start_time, end_time


def ask_for_time(prompt: str) -> str:
    """ Ask the user for a valid start and end time. """
    time = input(prompt)
    while True:
        if "s" in time or "m" in time:
            time = convert_to_timestamp(time)
            break
        elif re.search(r"\d+:\d+", time):
            break
        time = input("Wrong input...\n" + prompt)
    return time


def generate_output_filename(filename: str, tool_suffix: str) -> str:
    """ Generates the new filename with a suffix. """
    if filename.endswith("mp4"):
        return filename.replace(".mp4", f"{tool_suffix}.mp4")
    elif filename.endswith("mkv"):
        return filename.replace(".mkv", f"{tool_suffix}.mkv")
    else:
        return filename

