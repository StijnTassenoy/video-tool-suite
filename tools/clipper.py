# Python Imports #
import os
import subprocess

# VideoToolSuite Imports #
from tools.base import BaseTool
from lib.logger import LOGGER
from lib.helpers import clear_screen, ask_start_and_end_time, generate_output_filename, select_video_files


class Clipper(BaseTool):
    """
        Clipper tool.
        Create a clip out of the video, using start and end times.
    """

    def __init__(self, working_directory: str):
        self.working_directory = working_directory

    @classmethod
    def check_tool(cls, tool_option: str) -> bool:
        """ Returns True for the selected tool option in the menu. """
        return tool_option in cls.__name__

    @staticmethod
    def __clip_video(input_path: str, output_path: str, start_time: str, end_time: str) -> None:
        """ FFMPEG Clip command. """
        ffmpeg_command = ["ffmpeg"]
        ffmpeg_command += ["-ss", start_time]
        ffmpeg_command += ["-i", input_path]
        ffmpeg_command += ["-to", end_time]
        ffmpeg_command += ["-copyts"]
        ffmpeg_command += [output_path]
        LOGGER.info(str(ffmpeg_command))
        subprocess.Popen(ffmpeg_command)

    def use_tool(self) -> None:
        """ Clipper's "main" function. """
        clear_screen()
        video_files = select_video_files(self.working_directory)
        if not video_files:
            LOGGER.warning("No usable files in directory.")
            return

        start_time, end_time = ask_start_and_end_time()

        for video_file in video_files:
            self.__clip_video(
                os.path.join(self.working_directory, video_file),
                os.path.join(self.working_directory, generate_output_filename(video_file, "_clipped")),
                start_time,
                end_time
            )
