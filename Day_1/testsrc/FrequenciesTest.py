import unittest
from Frequencies import Freq


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.freq = Freq()

    def test_openFile(self):
        try:
            self.freq.fileio.openFile("input.txt")
        except:
            self.fail()

    def test_update(self):
        self.freq.updateFrequency(1)
        self.assertEqual(1, self.freq.currentFreq)

    def test_checkRepeating(self):
        self.freq.frequencylist.append(1)
        self.assertTrue(self.freq.checkRepeat(1))

    def test_getRepeatingFreq(self):
       print(self.freq.getRepeatingFreq("input.txt"))

if __name__ == '__main__':
    unittest.main()
