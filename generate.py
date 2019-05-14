from OpenGL.GLUT import *
from settings import *
import random

def rocksGen():
    global testRandom
    global generating
    global fCoin , fRock
    global cubeA
    global objects, rocks, coins, collisionCoins

    # Dictionary has types of objects
    types = {1: "rock", 2: "coin"}

    if testRandom:
        for i in range(0, 60):
            # Random positions of rocks in x-axis
            x = random.randrange(-2, 2)
            objects.xPoint(x)
            rockType = random.randrange(1, 3)
            generating.append(rockType)

    # Distance between each rocks along -z
    deltazRock = -6
    # Pointer of rock type and counter for x positions in xObjects
    rockPos = 0

    while rockPos < 60:

        if types[generating[rockPos]] == "rock":
            glColor3f(.6, 0.3, 0)
            glTranslate(objects.xPos()[rockPos], -1, deltazRock)
            glutSolidSphere(rockRadius, 20, 20)
            glLoadIdentity()

            if fRock:
                rocks.xPoint(objects.xPos()[rockPos])
                rocks.zPoint(deltazRock)

        if types[generating[rockPos]] == "coin":
            # Disappear the coin as long as coin collision is active
            if deltazRock in collisionCoins.zPos():
                glColor4f(1, 1, 0.1, 0)
                glTranslate(objects.xPos()[rockPos], -30, deltazRock)
                glScale(0.3, 0.3, 0.3)
                glutSolidTorus(innerR, outerR, 50, 50)
                glLoadIdentity()
            else:
                # Normal state of coins
                glColor4f(1, 1, 0.1, 1)
                glTranslate(objects.xPos()[rockPos] , -0.5, deltazRock)
                glScale(0.3, 0.3, 0.3)
                glutSolidTorus(innerR, outerR, 50, 50)
                glLoadIdentity()

            if fCoin:
                coins.xPoint(objects.xPos()[rockPos])
                coins.zPoint(deltazRock)

        deltazRock -= 2
        rockPos = rockPos+1

    testRandom = False
    fCoin = False
    fRock = False