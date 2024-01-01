import unittest
from hashr.hashr import hashr

class TestHashr(unittest.TestCase):
    def test_hashr(self):
        result = hashr("Hello World!")
        self.assertEqual(result, "brclfmetdrenfrctfpesdnckfojt")

    def test_saltr(self):
        pass

if __name__ == "__main__":
    unittest.main()
