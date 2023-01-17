# Python Imports #
import os
import re
import subprocess

# VideoToolSuite Imports #
from tools.base import BaseTool
from lib.logger import LOGGER
from lib.helpers import clear_screen, ask_start_and_end_time, generate_output_filename, select_video_files


class ChangeAspectRatio(BaseTool):
    """
        Aspect Ratio Changer tool.
        Change the aspect ratio for video('s).
    """

    def __init__(self, working_directory: str):
        self.working_directory = working_directory

    @classmethod
    def check_tool(cls, tool_option: str) -> bool:
        """ Returns True for the selected tool option in the menu. """
        return tool_option in cls.__name__

    @staticmethod
    def __change_dar_video(input_path: str, output_path: str, aspect_ratio: str):
        """ FFMPEG change Display Aspect Ratio (METADATA) command. """
        ffmpeg_command = ["ffmpeg"]
        ffmpeg_command += ["-i", input_path]
        ffmpeg_command += ["-aspect", aspect_ratio]
        ffmpeg_command += [output_path]
        LOGGER.info(str(ffmpeg_command))
        subprocess.Popen(ffmpeg_command)

    @staticmethod
    def __change_sar_video(input_path: str, output_path: str, aspect_ratio: str):
        """ FFMPEG change Sample Aspect Ratio (PIXELS) command. """
        ffmpeg_command = ["ffmpeg"]
        ffmpeg_command += ["-i", input_path]
        ffmpeg_command += ["-vf", f"scale={aspect_ratio}"]
        ffmpeg_command += [output_path]
        LOGGER.info(str(ffmpeg_command))
        subprocess.Popen(ffmpeg_command)

    def use_tool(self) -> None:
        """ Aspect Ratio Changer's "main" function. """
        clear_screen()
        video_files = select_video_files(self.working_directory)
        if not video_files:
            LOGGER.warning("No usable files in directory.")
            return

        a_r = input("Enter the aspect ratio: ").lower()
        while not re.compile(r"\d+[:x]\d+").match(a_r):
            print("Wrong input...")
            a_r = input("Enter the aspect ratio: ").lower()
        if "x" in a_r:
            a_r = a_r.replace("x", ":")

        s_d = input("Sample Aspect Ratio or Display Aspect Ratio?\nType: SAR or DAR: ").lower()
        while True:
            if "sar" in s_d:
                for video_file in video_files:
                    self.__change_sar_video(
                        os.path.join(self.working_directory, video_file),
                        os.path.join(self.working_directory, generate_output_filename(video_file, "_NewAspectRatio")),
                        a_r
                    )
                break
            elif "dar" in s_d:
                for video_file in video_files:
                    self.__change_dar_video(
                        os.path.join(self.working_directory, video_file),
                        os.path.join(self.working_directory, generate_output_filename(video_file, "_NewAspectRatio")),
                        a_r
                    )
                break
            else:
                print("Wrong input...")
                s_d = input("Sample Aspect Ratio or Display Aspect Ratio?\nType: [SAR] or [DAR]")
