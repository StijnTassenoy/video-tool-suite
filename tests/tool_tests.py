import unittest

from tools import get_tool_classes


class TestTools(unittest.TestCase):
    def test_get_toolnames(self):
        expected_list = ["Clipper"]
        tool_name_list = [subclass.__name__ for subclass in get_tool_classes()]
        self.assertEqual(expected_list, tool_name_list)


if __name__ == '__main__':
    unittest.main()