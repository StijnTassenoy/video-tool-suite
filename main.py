import os
from typing import List

from lib.helpers import clear_screen, get_all_videofiles_from_directory,  print_files_with_index
from lib.constants import WELCOME_MESSAGE
from lib.logger import LOGGER
from tools import get_tool_classes
from tools.base import BaseTool

from rich import print as rprint
from rich.traceback import install

install()
working_directory = ""

#TODO, change to subclasses
tools_list = ["Clipper"]


def print_menu() -> None:
    if os.path.isdir(working_directory):
        print(f"\nCurrent directory: {str(working_directory)}\n")

    else:
        rprint(f"\nCurrent directory: [bold red]Not Set![/bold red]\n")
    rprint("[bold blue][1][/bold blue] Set directory")
    rprint("[bold blue][2][/bold blue] Choose tool")
    rprint("[bold blue][0][/bold blue] Exit")


def print_tools() -> List:
    tools = get_tool_classes()
    tools_name_list = []
    for idx, tool in enumerate(tools):
        rprint(f"[bold blue][{idx+1}][/bold blue] {tool.__name__}")
        tools_name_list.append(tool.__name__)
    return tools_name_list


# Option 1
def set_directory() -> None:
    global working_directory
    working_directory = input("Input new directory: ")
    while True:
        if os.path.isdir(working_directory) and not "":
            print(f"Working directory has been set!\n{working_directory}")
            break
        else:
            clear_screen()
            working_directory = input("Invalid directory...\nInput new directory: ")


# Option 2
def choose_tool() -> None:
    # video_files = get_all_videofiles_from_directory(working_directory, ["mp4", "mkv"])
    # print_files_with_index(video_files)
    # print(BaseTool.__subclasses__())
    tools_name_list = print_tools()
    tool_choice = input("Choose a tool: ")
    while True:
        if int(tool_choice)-1 in range(len(tools_name_list)) and not "":
            for tool in get_tool_classes():
                if tool.check_tool(tools_name_list[int(tool_choice)-1]):
                    try:
                        t = tool(working_directory)
                    except Exception as e:
                        LOGGER.exception(e)
            break
        else:
            clear_screen()
            tool_choice = input("Invalid Tool Choice! Choose a tool: ")


def main():
    while True:
        clear_screen()
        print(WELCOME_MESSAGE)
        print_menu()
        choice = input("\nEnter your choice: ")
        if choice == "1":
            clear_screen()
            set_directory()
        elif choice == "2" and os.path.isdir(working_directory):
            clear_screen()
            choose_tool()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")
    exit()


if __name__ == "__main__":
    main()
