from .base import BaseTool
from tools.clipper import Clipper
from tools.change_aspect_ratio import ChangeAspectRatio


def get_tool_classes():
    return BaseTool.__subclasses__()
