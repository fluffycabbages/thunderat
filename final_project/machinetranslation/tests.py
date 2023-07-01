import unittest
from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('hello'), 'Bonjour')
        self.assertNotEqual(english_to_french(0),0 )

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('bonjour'), 'bonjour')

unittest.main()