import os
import re
import numpy as np
from FileIO import fileIO

class FabricClaims:

    def __init__(self):
        self.fileio = fileIO(os.getcwd())
        self.claims = dict()
        self.grid = np.zeros((1000, 1000))

    def parsedata(self, data):
        return re.findall(r'\d+', data)

    def fillclaims(self, filename):
        self.fileio.openFile(filename)
        for line in self.fileio.file:
            claimdata = self.parsedata(line)
            self.claims[int(claimdata[0])] = [int(claimdata[1]), int(claimdata[2]), int(claimdata[3]), int(claimdata[4])]
        self.fileio.file.close()

#claim[key]: id, claim[0]: distance from left, claim[1]: distance from top, claim[2]:width, claim[3]: height

    def plotclaim(self, claim, id):
        posx = claim[0]
        posy = claim[1]
        for i in range(claim[2]):
            for j in range(claim[3]):
                if self.checkvaluesequal(self.grid[posx + i, posy + j], 0):
                    self.grid[posx+i, posy+j] = id
                else:
                    self.grid[posx+i, posy+j] = -1

    def plotclaims(self, filename):
        self.fillclaims(filename)
        for key, value in self.claims.items():
            self.plotclaim(value, key)

    def countconflicts(self):
        conflictcounter = 0
        for i in range(np.size(self.grid, 0)):
            for j in range(np.size(self.grid, 1)):
                if self.checkvaluesequal(self.grid[i, j], -1):
                    conflictcounter += 1
        return conflictcounter

    def checkvaluesequal(self, actual, expected):
        return actual == expected













