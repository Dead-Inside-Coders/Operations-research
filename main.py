import math as math
import numpy as np
import random


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


if __name__ == '__main__':
    # func1()
    func2()
