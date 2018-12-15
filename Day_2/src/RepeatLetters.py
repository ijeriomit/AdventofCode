import os

from FileIO import fileIO


class RepeatLetter:

    def __init__(self):
        self.fileio = fileIO(os.getcwd())

    def findSimialarStrings(self, filename):
        self.fileio.openFile(filename)
        lines = self.fileio.file.readlines()
        for i in range(len(lines)):
            for j in range(i+1, len(lines)):
                if self.areStringsSimialar(lines[i], lines[j]):
                    self.fileio.file.close()
                    return lines[i], lines[j]
        self.fileio.file.close()

    def removeDifferentLettersFromSimilarStrings(self, string1, string2):
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                return string1[:i] + string1[(i+1):]

    def areStringsSimialar(self, string1, string2):
        diffcount =0
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                diffcount += 1
                if diffcount > 1:
                    return False
        return True

    def countRepeats(self, filename):
        repeat2, repeat3 = 0, 0
        self.fileio.openFile(filename)
        for line in self.fileio.file:
            temp1, temp2 = self.getOccurences(line)
            repeat2 += temp1
            repeat3 += temp2
        self.fileio.file.close()
        return repeat2 * repeat3

    def getOccurences(self, string):
        hasTwo, hasThree = 0, 0
        for i in string:
            count = self.countLetterOccurences(i, string)
            if count == 2:
                hasTwo = 1
            elif count == 3:
                hasThree = 1
            if hasTwo == 1 & hasThree == 1:
                break
        return hasTwo, hasThree

    def countLetterOccurences(self, let, string):
        count = 0
        for i in string:
            if i == let:
                count += 1
                if count > 3:
                    return count
        return count

def main():

    repeatletters = RepeatLetter()
    print("CheckSum:", repeatletters.countRepeats("input.txt"))
    string1, string2 = repeatletters.findSimialarStrings("input.txt")
    print("Similar Strings:", string1, string2)
    print("Common Letters:", repeatletters.removeDifferentLettersFromSimilarStrings(string1, string2))

main()
