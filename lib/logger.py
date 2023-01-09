# Python Imports #
import sys
import logging

# Video-Tool-Suite Imports #
from settings import DEBUG


class Logger:
    """
        Custom logger for the Video-Tool-Suite.
    """

    def __init__(self):
        logging.basicConfig(
            format="%(asctime)s [%(levelname)s] %(thread)d <%(module)s.%(funcName)s> %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[
                logging.StreamHandler(sys.stdout),
            ]
        )
        self.logger = logging.getLogger("videotoolsuite_logger")
        self.check_log_level()

    def check_log_level(self):
        """ Checks if the --debug parameter is set and sets the loglevel accordingly. """
        if DEBUG:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)

    def info(self, msg):
        """ Report events that occur during normal operation of the toolsuite. """
        self.logger.info(msg)

    def debug(self, msg):
        """ Report events that occur during debugging. """
        self.logger.debug(msg)

    def warning(self, msg):
        """ Issue a warning regarding a particular runtime event. """
        self.logger.debug(msg)

    def error(self, msg):
        """ Report suppression of an error without raising an exception. """
        self.logger.debug(msg)

    def exception(self, msg):
        """ Report suppression of an error without raising an exception. """
        self.logger.debug(msg)


LOGGER = Logger()
