# Python Imports #
from abc import ABCMeta, abstractmethod


class BaseTool(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, working_directory: str):
        pass

    @classmethod
    @abstractmethod
    def get_toolname(cls) -> str:
        pass
