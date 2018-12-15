import os
import re
import numpy as np
from FileIO import fileIO

class FabricClaims:

    def __init__(self):
        self.fileio = fileIO(os.getcwd())
        self.grid = np.zeros((1000, 1000))
        self.conflicts = list()
        self.claims = dict()

    def fillclaims(self, filename):
        self.fileio.openFile(filename)
        for line in self.fileio.file:
            claimdata = parsedata(line)
            self.claims[int(claimdata[0])] = [int(claimdata[1]), int(claimdata[2]), int(claimdata[3]), int(claimdata[4])]
        self.fileio.file.close()
        return self.claims

    def plotclaims(self, claims):
        for key, value in claims.items():
            self.plotclaim(value, key)

    # claim[key]: id, claim[0]: distance from left, claim[1]: distance from top, claim[2]:width, claim[3]: height
    def plotclaim(self, claim, id):
        posx = claim[0]
        posy = claim[1]
        for i in range(claim[2]):
            for j in range(claim[3]):
                if checkvaluesequal(self.grid[posx + i, posy + j], 0):
                    self.grid[posx+i, posy+j] = id
                else:
                    self.storeconflict(self.grid[posx+i, posy+j], id)
                    self.grid[posx+i, posy+j] = -1

    def storeconflict(self, id1, id2):
        if id1 not in self.conflicts:
            self.conflicts.append(id1)
        if id2 not in self.conflicts:
            self.conflicts.append(id2)

    def countconflictinginchesongrid(self):
        conflictcounter = 0
        for i in range(np.size(self.grid, 0)):
            for j in range(np.size(self.grid, 1)):
                if checkvaluesequal(self.grid[i, j], -1):
                    conflictcounter += 1
        return conflictcounter

    def findNonConflictingclaim(self, claims, conflicts):
        for key, value in claims.items():
            if key not in conflicts:
                return key

def parsedata(data):
    return re.findall(r'\d+', data)

def checkvaluesequal(actual, expected):
    return actual == expected



def main():
    fabclaim = FabricClaims()
    fabclaim.fillclaims("input.txt")
    fabclaim.plotclaims(fabclaim.claims)
    print(fabclaim.countconflictinginchesongrid())
    print(fabclaim.findNonConflictingclaim(fabclaim.claims, fabclaim.conflicts))















