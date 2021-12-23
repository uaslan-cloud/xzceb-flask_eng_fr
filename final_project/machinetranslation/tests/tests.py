import unittest
from translator import english_to_french, french_to_english

class TestsEnglishToFrench(unittest.TestCase):
    """
    Class 
    """
    def test1(self):
        """
        test englishtofrench
        """
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Bonjour"), "Hello")

class TestsFrenchToEnglish(unittest.TestCase):
    """
    Class 
    """
    def test1(self):
        """
        test frenchtoenglish
        """
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Hello"), "Bonjour")

unittest.main()