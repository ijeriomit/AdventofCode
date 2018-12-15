import os

class fileIO:

    def __init__(self, path):
        self.file = None
        self.directorypath = self.getCurrentDirectoryPath(path)

    def getCurrentDirectoryPath(self, path):
        return os.path.dirname(path)

    def openFile(self, filename):
        self.file = open(os.path.join(self.directorypath, filename), "r")
