import random


def getRandom(start, end):
    n = random.randint(start, end)
    return n


print("The Random number is ", getRandom(10, 1000))
