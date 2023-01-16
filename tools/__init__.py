from .base import BaseTool
from tools.clipper import Clipper


def get_tool_classes():
    return BaseTool.__subclasses__()
