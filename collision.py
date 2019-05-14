from math import *
from settings import *

def rockCollision(cubeWidth, cubeLength, radB, x, z):
    global cubeA

    halfWidth = cubeWidth / 2
    halfLength = cubeLength / 2

    right = cubeA[0] + halfWidth
    left = cubeA[0] - halfWidth
    top = cubeA[2] - halfLength
    bottom = cubeA[2] + halfLength

    for i in range(len(x)):
        if x[i] >= right:
            collisionX = right
        else:
            if x[i] <= left:
                collisionX = left
            else:
                collisionX = x[i]

        if (z[i] <= top):
            collisionZ = top
        else:
            if z[i] >= bottom:
                collisionZ = bottom
            else:
                collisionZ = z[i]

        diffX = collisionX - x[i]
        diffZ = collisionZ - z[i]
        distance = pow(diffX, 2) + pow(diffZ, 2)

        if sqrt(distance) <= radB:
            return True

    return False


def coinCollision(cubeWidth, cubeLength, radB, x, z):
    global cubeA
    global coins
    global collisionCoins

    halfWidth = cubeWidth / 2
    halfLength = cubeLength / 2

    right = cubeA[0] + halfWidth
    left = cubeA[0] - halfWidth
    top = cubeA[2] - halfLength
    bottom = cubeA[2] + halfLength

    for i in range(len(x)):
        if x[i] >= right:
            collisionX = right
        else:
            if x[i] <= left:
                collisionX = left
            else:
                collisionX = x[i]

        if (z[i] <= top):
            collisionZ = top
        else:
            if z[i] >= bottom:
                collisionZ = bottom
            else:
                collisionZ = z[i]

        diffX = collisionX - x[i]
        diffZ = collisionZ - z[i]
        distance = pow(diffX, 2) + pow(diffZ, 2)

        if sqrt(distance) <= radB and (coins.zPos()[i] not in collisionCoins.zPos()):
            collisionCoins.zPoint(coins.zPos()[i])
            return True

    return False


def collWithRightTerrain(x):
    if x >= 2.7947911189503065:
        return True


def collWithLeftTerrain(x):
    if x <= -2.8013183011457476:
        return True
