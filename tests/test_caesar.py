#requires that you add main project directory to your $PYTHONPATH
#probably a better solution


from cipherinterface import *
from caesar import *
import unittest


class TestCaesar(unittest.TestCase):

    def setUp(self):
        self.testEncString = 'test'
        self.testDecString = 'yjxy'
        self.testInterface = Caesar()
        self.testInterface.setKey(5)

    def test_Caesar_ENC(self):
        self.assertEqual(self.testInterface.encrypt(self.testEncString), self.testDecString)

    def test_Caesar_DEC(self):
        self.assertEqual(self.testInterface.decrypt(self.testDecString), self.testEncString)
