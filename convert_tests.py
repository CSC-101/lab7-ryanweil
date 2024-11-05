import unittest
from convert import str_to_float


class TestStrToFloat(unittest.TestCase):

    def test_valid_float_string(self):
        self.assertEqual(str_to_float("123.45"), 123.45)

    def test_valid_integer_string(self):
        self.assertEqual(str_to_float("100"), 100.0)

    def test_invalid_string(self):
        self.assertIsNone(str_to_float("abc"))

    def test_empty_string(self):
        self.assertIsNone(str_to_float(""))

    def test_string_with_spaces(self):
        self.assertIsNone(str_to_float(" 1 2 3 "))

    def test_special_characters(self):
        self.assertIsNone(str_to_float("!@#"))


if __name__ == '__main__':
    unittest.main()

