
class RepeatLetter:

    def __init__(self):
        self.file = None

    def openFile(self, filename):
        self.file = open("C:/Users/jerio/Documents/PycharmProjects/AdventofCode/Day_2/" + filename, "r")

    def findSimialarStrings(self, filename):
        self.openFile(filename)
        lines = self.file.readlines()
        for i in range(len(lines)):
            for j in range(i+1, len(lines)):
                index = self.areStringsSimialar(lines[i], lines[j])
                if index != -1:
                    return lines[i],lines[j], index

    def removeDifferentLetters(self, string, index):
        return string[:index] + string[(index+1):]

    def areStringsSimialar(self, string1, string2):
        diffcount =0
        index = -1
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                diffcount += 1
                index = i
                if diffcount > 1:
                    return -1
        return index

    def countRepeats(self, filename):
        repeat2, repeat3 =0, 0
        self.openFile(filename)
        for line in self.file:
            temp1, temp2 = self.getOccurences(line)
            repeat2 += temp1
            repeat3 += temp2
        self.file.close()
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



