import subprocess
from abc import abstractmethod

from lib.logger import LOGGER
from tools.base import BaseTool


class Clipper(BaseTool):

    def __init__(self, working_directory: str):
        self.working_directory = working_directory

    @classmethod
    def get_toolname(cls) -> str:
        return cls.__class__.__name__

    @staticmethod
    def __clip_video(input_path: str, output_path: str, start_time: str, end_time: str):
        ffmpeg_command = ["ffmpeg"]
        ffmpeg_command += ["-ss", start_time]
        ffmpeg_command += ["-i", input_path]
        ffmpeg_command += ["-to", end_time]
        ffmpeg_command += ["-copyts", output_path]
        LOGGER.debug(str(ffmpeg_command))
        subprocess.Popen(ffmpeg_command)


