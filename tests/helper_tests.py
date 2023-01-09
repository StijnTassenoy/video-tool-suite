import unittest
from lib.helpers import convert_to_timestamp, convert_timestamp_to_seconds


class TestHelpers(unittest.TestCase):
    def test_convert_seconds_to_timestamp(self):
        # Testing seconds conversion
        self.assertEqual("00:00:00", convert_to_timestamp("0s"))
        self.assertEqual("01:01:01", convert_to_timestamp("3661s"))
        self.assertEqual("24:00:00", convert_to_timestamp("86400s"))

    def test_convert_minutes_to_timestamp(self):
        # Testing minutes conversion
        self.assertEqual("00:00:00", convert_to_timestamp("0m"))
        self.assertEqual("01:01:00", convert_to_timestamp("61m"))
        self.assertEqual("24:00:00", convert_to_timestamp("1440m"))

    def test_convert_timestamp_to_seconds(self):
        # Testing timestamp conversion
        self.assertEqual("0s", convert_timestamp_to_seconds("00:00:00"))
        self.assertEqual("3661s", convert_timestamp_to_seconds("01:01:01"))
        self.assertEqual("86400s", convert_timestamp_to_seconds("24:00:00"))


if __name__ == '__main__':
    unittest.main()