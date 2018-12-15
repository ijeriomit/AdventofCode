import os

from FileIO import fileIO


class Freq:

    def __init__(self):
        self.fileio = fileIO(os.getcwd())
        self.currentFreq = 0
        self.frequencylist = [0]

    def getFinalFreq(self, filename):
        self.fileio.openFile(filename)
        for line in self.fileio.file:
            self.updateFrequency(int(line))
        self.fileio.file.close()

    def getRepeatingFreq(self, filename):
        self.fileio.openFile(filename)
        i = 0
        while True:
            for line in self.fileio.file:
                self.updateFrequency(int(line))
                if self.checkRepeat(int(self.currentFreq)):
                    self.fileio.file.close()
                    return self.currentFreq
            i += 1
            self.fileio.file.seek(0)

    def checkRepeat(self, val):
        if val not in self.frequencylist:
            self.frequencylist.append(val)
            return False
        else:
            return True

    def updateFrequency(self, val):
        self.currentFreq += val


def main():
    freq = Freq()
    freq.getFinalFreq("input.txt")
    print("Frequency:", freq.currentFreq)
    print("Repeating Frequency", freq.getRepeatingFreq("input.txt"))

