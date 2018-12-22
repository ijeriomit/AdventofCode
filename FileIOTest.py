import os
import unittest
from FileIO import fileIO

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.fileio = fileIO(os.getcwd())

    def test_openFile(self):
        try:
            self.fileio.openFile("input.txt")
        except:
            self.fail()

    def test_parseData(self):
        self.assertEqual(['1', '669', '271', '17', '11'], self.fileio.parsedata("#1 @ 669,271: 17x11", r'\d+'))


if __name__ == '__main__':
    unittest.main()
