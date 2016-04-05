# Author: Roland Gabriel
# @rolandgnm

import random


def printList(sourceList, randTestElem):
    i = 1
    for elem in sourceList:
        print elem, euclideanDist(elem, randTestElem)
        i += 1


def parseFloats(matrix):
    for currL in matrix:
        for idx, param in enumerate(currL):
            try:
                currL[idx] = float(param)
            except:
                pass


def euclideanDist(currList, sourceList):
    res = 0
    for param, source in zip(currList, sourceList):
        try:
            res += (param - source) ** 2
        except:
            pass
    return res ** 0.5


if __name__ == '__main__':
    fileName = 'iris.data'
    chunckPercentage = 0.2

    # Parse file into list of floats and string
    dataList = [line.strip().split(',') for line in open(fileName, 'r')]
    parseFloats(dataList)

    # Generate Random list from dataList
    testList = [random.choice(dataList) for _ in range(
        int(len(dataList)*chunckPercentage))]

    # Choose Random Test Element
    randTestElem = random.choice(testList)

    print '## Test Element: ', randTestElem, ' ##\n\n'

    # Sort list by Euclidian Distance
    sortedList = sorted(testList, key=lambda currList: euclideanDist(
        currList, randTestElem))
    # Pop randTestElem
    sortedList.pop(0)

    printList(sortedList[0:5], randTestElem)
