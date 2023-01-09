# Python Imports #
import argparse

parser = argparse.ArgumentParser(description="Optional command line parameters for the video-tool-suite.")
parser.add_argument("-d", "--debug",
                    help="Turn on debug-mode.",
                    action="store_true")
argument = parser.parse_args()

DEBUG = argument.debug
