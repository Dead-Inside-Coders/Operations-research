import math as math
import numpy as np
import random
import os


def func1():
    print("Laba 1")
    print("Variant 9 :", (3.1 + 3.4) * 3.8)
    print("Variant 8 :", (4 / 11) / (-16 / 33) + 5 * (3 / 4))
    print("Variant 2 :",
          ((math.pow(2, 5) * (12.3 + 52.7 * (31 / math.pow(73, 2.5)))) * (12.3 - 52.7 * (31 / math.pow(73, 2.5)))) /
          (math.pow(123 + 527 * (31 / math.pow(73, 2)), (1 / 3)) + 233)
          )
    print("Ticket")
    string = input("Enter a number with four digits: \n")
    num = int(string)
    if num % 2 != 0:
        raise Exception("not even")
    splitIndex = string.__len__() / 2
    firstTowNumber = 0
    secondTowNumber = 0
    for i in range(0, int(splitIndex)):
        firstTowNumber += int(string[i])
    for e in range(int(splitIndex), string.__len__()):
        secondTowNumber += int(string[e])

    if firstTowNumber == secondTowNumber:
        print("Lucky ticket")
    elif firstTowNumber - secondTowNumber == 1 or firstTowNumber - secondTowNumber == -1:
        print("Half Lucky ticket")
    else:
        print("Simple ticket")


def getInfoFromArray(array):
    print("Max value in mass: " + str(max(array)))
    print("Min value in mass: " + str(min(array)))
    print("Sum of elements in mass: " + str(sum(array)) + "\n")


def func2():
    size = int(input("Enter mass size: \n"))
    mass = []
    for i in range(0, size):
        print("Enter number " + str(i + 1) + " out of " + str(size))
        mass.append(int(input()))
    getInfoFromArray(mass)
    generatedMass = []
    for i in range(0, size):
        generatedMass.append(random.randint(0, 100))
    getInfoFromArray(generatedMass)

    print(np.array([1, 2, 3, 4, 5]))
    print(np.zeros(5))
    print(np.arange(0, 5))


def readFile(fileName):
    filehandle = open(fileName)
    file = filehandle.read()
    mass = file.split("\n")
    twoDimMass = []
    for i in range(0, len(mass)):
        temp = mass[i].split(" ")
        temp1 = []
        for j in range(0, len(temp)):
            temp1.append(int(temp[j]))
        twoDimMass.append(temp1)
    filehandle.close()
    return twoDimMass


def task3():
    twoDimensionalArray = readFile('input1.txt')
    sum = twoDimensionalArray[0][0]
    step = Step(0, 0)
    move = Move
    array = []
    while len(twoDimensionalArray) != step.x + 1 or len(twoDimensionalArray[0]) != step.y + 1:
        step = move.doStep(twoDimensionalArray, step)
        array.append(step)
    for item in array:
        sum += twoDimensionalArray[item.x][item.y]
    print("Sum: " + str(sum))


class Move:
    def doStep(twoDimensionalArray, step):
        sumDown = goDown(twoDimensionalArray, step)
        sumRight = goRight(twoDimensionalArray, step)
        if sumDown > sumRight:
            return Step(step.x + 1, step.y)
        elif sumDown < sumRight:
            return Step(step.x, step.y + 1)
        elif sumRight == sumRight and sumRight > 0:
            return Step(step.x, step.y + 1)
        else:
            return Step(step.x, step.y)


def goDown(twoDimensionalArray, step):
    if len(twoDimensionalArray) > step.x + 1:
        return twoDimensionalArray[step.x + 1][step.y]
    else:
        return 0


def goRight(twoDimensionalArray, step):
    if len(twoDimensionalArray[step.x]) > step.y + 1:
        return twoDimensionalArray[step.x][step.y + 1]
    else:
        return 0


class Step:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getXposition(self):
        return self.x

    def getYposition(self):
        return self.y

    def setXposition(self, x):
        self.x = x

    def setYposition(self, y):
        self.y = y


if __name__ == '__main__':
    # func1()
    # func2()
    task3()
