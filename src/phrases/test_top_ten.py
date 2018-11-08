import unittest
from unittest.mock import patch
from phrases import top_ten


class TestTopTen(unittest.TestCase):

    @patch.object(top_ten, "raw_input", create=True)
    def test_using_decorator(self, raw_input):
        raw_input.return_value = input_data = "123"
        expected = int(input_data)

        actual = top_ten.main()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
