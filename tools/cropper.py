# Python Imports #
import os
import subprocess

# VideoToolSuite Imports #
from tools.base import BaseTool
from lib.logger import LOGGER
from lib.helpers import clear_screen, generate_output_filename, select_video_files, \
    ask_for_crop_dimensions, get_video_dimensions


class Cropper(BaseTool):
    """
        Cropper tool.
        Crop a video by inputting crop dimensions.
    """

    def __init__(self, working_directory: str):
        self.working_directory = working_directory

    @classmethod
    def check_tool(cls, tool_option: str) -> bool:
        """ Returns True for the selected tool option in the menu. """
        return tool_option in cls.__name__

    @staticmethod
    def __crop_video(input_path: str, output_path: str, width: str, bottom: str, cut_left: str, cut_right: str) -> None:
        """ FFMPEG Crop command. """
        ffmpeg_command = ["ffmpeg"]
        ffmpeg_command += ["-i", input_path]
        ffmpeg_command += ["-vf", f"crop={width}:{bottom}:{cut_left}:{cut_right}"]
        ffmpeg_command += ["-c:v", "libx264"]
        ffmpeg_command += ["-crf", "0"]
        ffmpeg_command += ["-c:a", "copy"]
        ffmpeg_command += [output_path]
        LOGGER.info(str(ffmpeg_command))
        subprocess.Popen(ffmpeg_command)

    def use_tool(self) -> None:
        """ Cropper's "main" function. """
        clear_screen()
        video_files = select_video_files(self.working_directory, dimensions_needed=True)
        if not video_files:
            LOGGER.warning("No usable files in directory.")
            return

        cut_from_top, cut_from_left, cut_from_right, cut_from_bottom = ask_for_crop_dimensions()

        for video_file in video_files:
            width, height = get_video_dimensions(os.path.join(self.working_directory, video_file))
            width -= int(cut_from_left)
            width -= int(cut_from_right)
            bottom = str(float(height) - float(cut_from_bottom) - float(cut_from_top))[:-2]
            self.__crop_video(
                os.path.join(self.working_directory, video_file),
                os.path.join(self.working_directory, generate_output_filename(video_file, "_cropped")),
                str(width),
                str(bottom),
                str(cut_from_left),
                str(cut_from_right)
            )
