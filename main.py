import os
from lib.helpers import clear_screen, get_all_videofiles_from_directory,  print_files_with_index
from lib.constants import WELCOME_MESSAGE
from lib.logger import LOGGER

from rich import print as rprint
from rich.traceback import install

install()
working_directory = ""


def print_menu():
    if os.path.isdir(working_directory):
        print(f"\nCurrent directory: {str(working_directory)}\n")

    else:
        rprint(f"\nCurrent directory: [bold red]Not Set![/bold red]\n")
    rprint("[bold blue][1][/bold blue] Set directory")
    rprint("[bold blue][2][/bold blue] Choose tool")
    rprint("[bold blue][0][/bold blue] Exit")


def set_directory():
    global working_directory
    working_directory = input("Input new directory: ")
    while True:
        if os.path.isdir(working_directory) and not "":
            print(f"Working directory has been set!\n{working_directory}")
            break
        else:
            clear_screen()
            working_directory = input("Invalid directory...\nInput new directory: ")


def choose_tool():
    video_files = get_all_videofiles_from_directory(working_directory, ["mp4", "mkv"])
    print_files_with_index(video_files)
    input()


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
