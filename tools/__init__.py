from .base import BaseTool
from tools.clipper import Clipper
from tools.cropper import Cropper
from tools.change_aspect_ratio import ChangeAspectRatio
from tools.trimmer import Trimmer
from tools.audio_track_remover import AudioTrackRemover


def get_tool_classes():
    return BaseTool.__subclasses__()
