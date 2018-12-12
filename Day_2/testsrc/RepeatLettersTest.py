import unittest
from RepeatLetters import RepeatLetter

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.rl = RepeatLetter()

    def test_count3similiar(self):
        self.assertTrue(self.rl.hasThreeRepeat("aaabbn"))

    def test_countOccurencewith3(self):
        self.assertEqual(3, self.rl.countLetterOccurences("a", "aaabb"))

    def test_countOccurencewith2(self):
        self.assertEqual(2, self.rl.countLetterOccurences("a", "aabb"))

    def test_countOccurencegreaterthan3(self):
        self.assertTrue(self.rl.countLetterOccurences("a", "aaaabb") > 3)

    def test_countOccurencebinumber(self):
        self.assertTrue(self.rl.countLetterOccurences("b", "abbbbbbb") > 3)

    def test_getOccurencesBothTrue(self):
        self.assertEqual((1, 1), self.rl.getOccurences("aabbb"))

    def test_getOccurenceshas2(self):
        self.assertEqual((1, 0), self.rl.getOccurences("aabcde"))

    def test_getOccurenceshas3(self):
        self.assertEqual((0, 1), self.rl.getOccurences("aaabcde"))

    def test_areStringSimialar(self):
        self.assertEqual(1, self.rl.areStringsSimialar("him", "hem"))

    def test_areStringsNotSimialar(self):
        self.assertEqual(-1, self.rl.areStringsSimialar("him", "her"))

    def test_areStringsNotSimialarManyDifferences(self):
        self.assertEqual(-1, self.rl.areStringsSimialar("hiiim", "heeer"))

    def test_findfamiliarStrings(self):
        tuple = self.rl.findSimialarStrings("input.txt")
        print(self.rl.removeDifferentLetters(tuple[0], tuple[2]))


if __name__ == '__main__':
    unittest.main()
