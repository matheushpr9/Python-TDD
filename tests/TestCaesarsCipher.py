import unittest
import string 
from modules.CaesarCipher import encrypt

class TestEncryption(unittest.TestCase):
    
    def setUp(self) -> None:
        self.message = "This is a secret!"

    def  test_inputExists(self):
        self.assertIsNotNone(self.message)

    def test_inputType(self):
        self.assertIsInstance(self.message, str)

    def test_functionReturnsSomething(self):
        self.assertIsNotNone(encrypt(self.message))

    def test_lenIO(self):
        self.assertEqual(len(self.message), len(encrypt(self.message)))

    def test_differentIO(self):
        self.assertNotIn(self.message, encrypt(self.message))

    def test_outputType(self):
        self.assertIsInstance(encrypt(self.message), str)
    
    def test_shiftedCipher(self):
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        encrypted_message = "".join([abc[abc.find(char)+1] if len(abc) >(abc.find(char)+1) else abc[0] for id, char in enumerate(self.message)])

        self.assertCountEqual(encrypted_message, encrypt(self.message))

    def test_shiftBy(self):
        shift_by = -4
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        encrypted_message = "".join([abc[abc.find(char)+shift_by] if len(abc) >(abc.find(char)+shift_by) else abc[0] for id, char in enumerate(self.message)])

        self.assertEqual(encrypted_message,encrypt(self.message, shift_by=shift_by))
                    

if __name__=="__main__":
    unittest.main()