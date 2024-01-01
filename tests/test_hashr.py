import unittest
from unittest.mock import patch, MagicMock
from hashr.hashr import hashr, saltr, number_to_letters, _main


class TestHashr(unittest.TestCase):
    def test_hashr(self):
        # test known hash result of "Hello World!"
        hash = hashr("Hello World!")
        empty_hash = hashr("")
        self.assertEqual(hash, "brclfmetdrenfrctfpesdnckfojt")
        self.assertEqual(empty_hash, "")

    def test_saltr(self):
        number_salt = int(saltr(False))
        letter_salt = saltr()
        self.assertLess(999999, number_salt)
        self.assertGreater(10000000, number_salt)
        self.assertIs(type(letter_salt), str)

    def test_number_to_letters(self):
        letters = number_to_letters(12345)
        zero = number_to_letters(0)
        self.assertEqual(letters, "alcne")
        self.assertEqual(zero, "j")

    @patch("builtins.print")
    @patch("sys.argv", ["test_hashr.py", "test_input", "-s"])
    @patch("hashr.hashr._main", MagicMock(side_effect=lambda x: "iqirioc"))
    def test_main_with_salt(self, mock_print):
        _main()
        expected_output = "Hash: esakanhqcpimgmencocpgnhtfnal\nSalt: iqirioc"
        mock_print.assert_called_once_with(expected_output)

    @patch("builtins.print")
    @patch("sys.argv", ["test_hashr.py", "test_input"])
    def test_main_without_salt(self, mock_print):
        _main()
        expected_output = "Hash: atfoamfpjpdqfkcndmgthmimengmj"
        mock_print.assert_called_once_with(expected_output)

    @patch("builtins.print")
    @patch("sys.argv", ["test_hashr.py", ""])
    def test_main_missing_input(self, mock_print):
        with self.assertRaises(SystemExit) as context:
            _main()
        self.assertEqual(context.exception.code, 1)
        mock_print.assert_called_once_with("Error: Input string is required.")


if __name__ == "__main__":
    unittest.main()
