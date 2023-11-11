import unittest

class TestEncryption(unittest.TestCase):
    
    def setUp(self) -> None:
        self.message = ""

    def  test_inputExists(self):
        self.assertIsNotNone(self.message)

    def test_inputType(self):
        self.assertIsInstance(self.message, str)

if __name__=="__main__":
    unittest.main()