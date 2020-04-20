import unittest

def is_palindrome(un_mot):
    for lettre in un_mot:
        print(lettre)
    return True

my_word = "kayak"
["k","a","y","a","k"]
my_word[0] == "k" #première lettre du mot
my_word[-1] == "k" #dernière lettre du mot

class PalindromeTest(unittest.TestCase):

    def test_word(self):
        self.assertEqual(True,is_palindrome("Kayak"))
        self.assertEqual(False,is_palindrome("toto"))