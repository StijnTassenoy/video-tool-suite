# Python Imports #
import os
import re
import subprocess
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


def print_files_with_index(file_list: List[str], working_directory: str, dimensions_needed: bool) -> None:
    """ Print all files from a list with their 1-based index. """
    for idx, file in enumerate(file_list):
        if dimensions_needed:
            width, height = get_video_dimensions(os.path.join(working_directory, file))
            dimensions = f" → {height}*{width}"
        else:
            dimensions = ""
        rprint(f"[bold blue][{str(idx+1)}][/bold blue] {file}[dim white]{dimensions}[/dim white]")


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


def select_video_files(working_directory: str, dimensions_needed=False) -> Optional[List[str]]:
    """ Select valid input for video files from a directory. """
    video_files = get_all_videofiles_from_directory(working_directory, (".mp4", ".mkv"))
    if len(video_files) == 1:
        print_files_with_index(video_files, working_directory, dimensions_needed)
        print()
        return video_files
    elif len(video_files) > 1:
        rprint("[bold blue][0][/bold blue] All files")
        print_files_with_index(video_files, working_directory, dimensions_needed)
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


def get_video_dimensions(file_path: str) -> tuple[int, int]:
    """ Use the ffprobe binaries to get the dimensions of a certain video """
    binary = "./binaries/ffprobe.exe"
    cmd = f"{binary} -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 \"{file_path}\""
    result = subprocess.run(cmd, capture_output=True, text=True)
    width, height = map(int, result.stdout.strip().split("x"))
    return width, height


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


def ask_for_crop_dimensions():
    """ Get valid dimensions to crop. """
    def input_validation(question: str) -> int:
        while True:
            value = input(question)
            if value.isnumeric():
                return int(value)
            print("Wrong input")

    cut_from_top = input_validation("Enter the number of pixels to crop from top: ")
    cut_from_left = input_validation("Enter the number of pixels to crop from left: ")
    cut_from_right = input_validation("Enter the number of pixels to crop from right: ")
    cut_from_bottom = input_validation("Enter the number of pixels to crop from bottom: ")
    return cut_from_top, cut_from_left, cut_from_right, cut_from_bottom


def generate_output_filename(filename: str, tool_suffix: str) -> str:
    """ Generates the new filename with a suffix. """
    if filename.endswith("mp4"):
        return filename.replace(".mp4", f"{tool_suffix}.mp4")
    elif filename.endswith("mkv"):
        return filename.replace(".mkv", f"{tool_suffix}.mkv")
    else:
        return filename

