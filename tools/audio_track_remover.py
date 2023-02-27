# Python Imports #
import os
import subprocess

# VideoToolSuite Imports #
from tools.base import BaseTool
from lib.logger import LOGGER
from lib.helpers import clear_screen, generate_output_filename, select_video_files, ask_start_and_end_trimming_time, \
    get_video_length, calculate_time_difference, convert_to_timestamp, input_int_validation, count_audio_streams


class AudioTrackRemover(BaseTool):
    """
        Audio Track Remover tool.
        Remove a certain audio track from a videofile.
    """

    def __init__(self, working_directory: str):
        self.working_directory = working_directory

    @classmethod
    def check_tool(cls, tool_option: str) -> bool:
        """ Returns True for the selected tool option in the menu. """
        return tool_option in cls.__name__

    @staticmethod
    def __remove_audio_track(input_path: str, output_path: str, streams_to_keep: str) -> None:
        """ MKVmerge track keeper command. """
        mkvmerge_command = ["mkvmerge"]
        mkvmerge_command += ["-o", output_path]
        mkvmerge_command += ["--atracks", streams_to_keep]
        mkvmerge_command += [input_path]
        LOGGER.info(str(mkvmerge_command))
        subprocess.Popen(mkvmerge_command)

    def use_tool(self) -> None:
        """ Clipper's "main" function. """
        clear_screen()
        video_files = select_video_files(self.working_directory, audiotrack_count_needed=True)
        if not video_files:
            LOGGER.warning("No usable files in directory.")
            return

        rmv_audiostream_num = input_int_validation("Enter audio stream number to remove:")

        for video_file in video_files:
            stream_arr = []
            audiostream_count = count_audio_streams(os.path.join(self.working_directory, video_file))
            for idx in range(1, audiostream_count + 1):
                stream_arr.append(idx)
            if rmv_audiostream_num in stream_arr:
                stream_arr.remove(rmv_audiostream_num)
            if len(stream_arr) == 1:
                streams_to_keep = str(stream_arr[0])
            else:
                streams_to_keep = ",".join(str(x) for x in stream_arr)
            self.__remove_audio_track(
                os.path.join(self.working_directory, video_file),
                os.path.join(self.working_directory, generate_output_filename(video_file, "_audioremoved")),
                streams_to_keep
            )
