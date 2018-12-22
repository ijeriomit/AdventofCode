
import unittest
from GuardShifts import GuardShift


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.guardshift = GuardShift()

    def test_getDateInfoLine1(self):
        self.assertEqual('0318',
                         self.guardshift.getDateInfo("[1518-03-18 00:03] Guard #3529 begins shift"))

    def test_getDateInfoLine2(self):
        self.assertEqual('0426',
                         self.guardshift.getDateInfo("[1518-04-26 00:55] wakes up"))

    def test_getDateInfoLine7(self):
        self.assertEqual('0408',
                         self.guardshift.getDateInfo("[1518-04-08 00:18] falls asleep"))

    def test_TimeInfoLine1(self):
        self.assertEqual('0003',
                         self.guardshift.getTimeInfo("[1518-03-18 00:03] Guard #3529 begins shift"))

    def test_TimeInfoLine2(self):
        self.assertEqual('0055',
                         self.guardshift.getTimeInfo("[1518-04-26 00:55] wakes up"))

    def test_TimeInfoLine7(self):
        self.assertEqual('0018',
                         self.guardshift.getTimeInfo("[1518-04-08 00:18] falls asleep"))

    def test_EventInfoLine1(self):
        self.assertEqual('Guard #3529 begins shift',
                         self.guardshift.getEventInfo("[1518-03-18 00:03] Guard #3529 begins shift"))

    def test_EventInfoLine2(self):
        self.assertEqual('wakes up',
                         self.guardshift.getEventInfo("[1518-04-26 00:55] wakes up"))

    def test_EventInfoLine7(self):
        self.assertEqual('falls asleep',
                         self.guardshift.getEventInfo("[1518-04-08 00:18] falls asleep"))

    def test_isgreater(self):
        self.assertTrue(self.guardshift.isgreaterthan("0018", "0003"))

    def test_isequal(self):
        self.assertTrue(self.guardshift.isequal("0018", "0018"))

    def test_isless(self):
        self.assertFalse(self.guardshift.isgreaterthan("0018", "0055"))

    def test_chronologicallygreater(self):
        self.assertTrue(self.guardshift.chronologicallygreater(("0426", "0055"), ("0318", "0003")))

    def testchronologicallyless(self):
        self.assertFalse(self.guardshift.chronologicallygreater(("0318", "0003"), ("0426", "0055")))

    def test_chronologicallyequal(self):
        self.assertTrue(self.guardshift.chronologicallyequal(("0318", "0003"), ("0318", "0003")))

    def test_sortbeginning(self):
        self.guardshift.saveGuardInfo("input.txt")
        records = self.guardshift.sortRecords(self.guardshift.recordslist)
        self.assertEqual([('0316', '0004', 'Guard #1973 begins shift'), ('0316', '0034', 'falls asleep'),
                          ('0316', '0039', 'wakes up')], [records[0], records[1], records[2]])



if __name__ == '__main__':
    unittest.main()
