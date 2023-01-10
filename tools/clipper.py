import subprocess
from lib.logger import LOGGER


def clip_video(input_path: str, output_path: str, start_time: str, end_time: str):
    ffmpeg_command = ["ffmpeg"]
    ffmpeg_command += ["-ss", start_time]
    ffmpeg_command += ["-i", input_path]
    ffmpeg_command += ["-to", end_time]
    ffmpeg_command += ["-copyts", output_path]
    LOGGER.debug(str(ffmpeg_command))
    subprocess.Popen(ffmpeg_command)


