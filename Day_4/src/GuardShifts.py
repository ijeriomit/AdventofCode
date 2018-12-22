import os
from FileIO import fileIO


class GuardShift:

    def __init__(self):
        self.fileio = fileIO(os.getcwd())
        self.recordslist = list()

    def getDateInfo(self, line):
        return self.fileio.parsedata(line, r'\d{2}-\d{2}\s')[0].replace("-", "").rstrip()
                #self.fileio.parsedata(line, r'\d{2}:\d{2}'),
                ###self.fileio.parsedata(line, r'[A-Za-z].+'))

    def getTimeInfo(self, line):
        return self.fileio.parsedata(line, r'\d{2}:\d{2}')[0].replace(":", "").rstrip()

    def getEventInfo(self, line):
        return self.fileio.parsedata(line, r'[A-Za-z].+')[0]

    def saveGuardInfo(self, filename):
        self.fileio.openFile(filename)
        for line in self.fileio.file:
            self.recordslist.append((self.getDateInfo(line), self.getTimeInfo(line), self.getEventInfo(line)))
        self.fileio.file.close()

    def isgreaterthan(self, time1, time2):
        return int(time1) > int(time2)

    def isequal(self, time1, time2):
        return int(time1) == int(time2)

    def chronologicallygreater(self, datetime1, datetime2):
        if self.isgreaterthan(datetime1[0], datetime2[0]):
            return True
        elif self.isequal(datetime1[0], datetime2[0]):
            return self.isgreaterthan(datetime1[1], datetime2[1])
        return False

    def chronologicallyequal(self, datetime1, datetime2):
        if self.isequal(datetime1[0], datetime2[0]):
            return self.isequal(datetime1[1], datetime2[1])

    def sortRecords(self, array):
        less = []
        equal = []
        greater = []
        if len(array) > 1:
            pivot = array[0]
            for x in array:
                if self.chronologicallygreater(pivot, x):
                    less.append(x)
                if self.chronologicallyequal(x, pivot):
                    equal.append(x)
                if self.chronologicallygreater(x, pivot):
                    greater.append(x)
            return self.sortRecords(less) + equal + self.sortRecords(greater)
        else:
            return array





