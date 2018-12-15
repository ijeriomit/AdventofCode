import unittest
from FabricCutter import FabricClaims

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.fabclaim = FabricClaims()

    def test_openFile(self):
        try:
            self.fabclaim.fileio.openFile("input.txt")
        except:
            self.fail()

    def test_parseDataLine1(self):
        self.fabclaim.fileio.openFile("input.txt")
        self.assertEqual(['1', '669', '271', '17', '11'], self.fabclaim.parsedata(self.fabclaim.fileio.file.readline()))

    def test_parseDataLine2(self):
        self.fabclaim.fileio.openFile("input.txt")
        self.fabclaim.fileio.file.readline()
        self.assertEqual(['2', '153', '186', '20', '26'], self.fabclaim.parsedata(self.fabclaim.fileio.file.readline()))

    def test_fillclaims(self):
        self.fabclaim.fillclaims("input.txt")
        self.assertEqual([669, 271, 17, 11], self.fabclaim.claims.get(1))

    def test_plotclaimsline1(self):
        self.fabclaim.fillclaims("input.txt")
        self.fabclaim.plotclaim(self.fabclaim.claims.get(1), 1)
        for i in range(17):
            for j in range(11):
                self.assertEqual(1, self.fabclaim.grid[669+i, 271+j])

    def test_plotclaimsline50(self):
        self.fabclaim.fillclaims("input.txt")
        claim = self.fabclaim.claims.get(50)
        self.fabclaim.plotclaim(claim, 50)
        for i in range(claim[2]):
            for j in range(claim[3]):
                self.assertEqual(50, self.fabclaim.grid[claim[0] + i, claim[1] + j])

    def test_countconfilicts(self):
        self.fabclaim.plotclaims("input.txt")
        print(self.fabclaim.countconflicts())

    def test_countconflicts(self):
        self.fabclaim.fillclaims("input.txt")


if __name__ == '__main__':
    unittest.main()
