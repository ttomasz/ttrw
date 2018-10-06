import unittest
import ttrw
from unittest.mock import patch

test_dictionary = {
    "en": {
        "adverbs": ["test"],
        "adjectives": ["test"],
        "nouns": ["test"]
    },
    "pl": {
        "adverbs": ["bardzo"],
        "adjectives": ["maly"],
        "nouns": ["ksiazka"]
    }
}


class TestTTRW(unittest.TestCase):

    def test_supported_language(self):
        for lang in ttrw.languages:
            s = ttrw.get_random_words(lang)
            self.assertGreater(len(s), 0)
            self.assertTrue(type(s) is str)

    def test_unsupported_language(self):
        self.assertRaises(ValueError, lambda: ttrw.get_random_words("xxx"))

    def test_fake_dic(self):
        with patch.dict("ttrw.words", test_dictionary):
            s = ttrw.get_random_words("en")
            self.assertEqual(s, "TestTestTest")

    def test_polish_gend(self):
        with patch.dict("ttrw.words", test_dictionary):
            s = ttrw.get_random_words("pl")
            self.assertEqual(s, "BardzoMalaKsiazka")


if __name__ == '__main__':
    unittest.main()
