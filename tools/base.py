# Python Imports #
from abc import ABCMeta, abstractmethod


class BaseTool(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, working_directory: str):
        pass

    @classmethod
    @abstractmethod
    def check_tool(cls, tool_option: str) -> bool:
        pass

    @abstractmethod
    def use_tool(self) -> bool:
        pass
