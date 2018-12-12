import inspect
import os
import Day_1

class Freq:

    def __init__(self):
        self.currentFreq = 0
        self.file = None
        self.frequencylist = [0]

    def getFinalFreq(self, filename):
        self.openFile(filename)
        for line in self.file:
            self.updateFrequency(int(line))
        self.file.close()

    def getRepeatingFreq(self, filename):
        self.openFile(filename)
        i =0
        while True:
            for line in self.file:
                self.updateFrequency(int(line))
                if self.checkRepeat(int(self.currentFreq)):
                    self.file.close()
                    return self.currentFreq
            i+=1
            self.file.seek(0)
        self.file.close()


    def openFile(self, filename):
        self.file = open("C:/Users/jerio/Documents/PycharmProjects/AdventofCode/Day_1/"+filename, "r")

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
    print("Repeating Frequency",freq.getRepeatingFreq("input.txt"))

main()

