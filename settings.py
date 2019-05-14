import numpy as np
from model import *
import pygame

VIEWPORT = (800, 600)
theta = 0

FPS = 60
previousTime = 0
dt = 0
pos = np.array([0, 0], dtype=np.float64)
vel = np.array([0, 0], dtype=np.float64)
acc = np.array([0, 0], dtype=np.float64)
cubeA = np.array([0, 0, 0], dtype=np.float64)
posz = 0

groundVertices1 = ((-5, -1, 20),(5, -1, 20),(5, -1, -300),(-5, -1, -300))
groundVertices2 = ((5, -1, 20),(30, -1, 20),(30, -1, -300),(5, -1, -300))
groundVertices3 = ((-5, -1, 20),(-30, -1, 20),(-30, -1, -300),(-5, -1, -300))

##### Collision cube #####
cubeWidth = 0.35
cubeLength = 1.9

##### Radius of rock #####
rockRadius = 0.3
trackRadius = 1
xTrackCenter = 4.5

##### Radius of coin #####
innerR = 0.5
outerR = 1

# To make random rocks only once in each time the game start
testRandom = True
# Test the rocks are collected only once
fRock = True
# Test the coins are collected only once
fCoin = True
# Test the game is ended
crashed = False
# Test the player reached to final destination
playerWin = False
# The score of player
score = 0

objects = Position()
rocks   = Position()
coins   = Position()
collisionCoins = Position()

# Storing the types of objects
generating = []

def sound():
    pygame.mixer.init(44100, -16, 2, 2048)
    pygame.mixer.music.load("sounds/row.WAV")
    pygame.mixer.music.play(-1)


def soundCoin():
    pygame.mixer.init(44100, -16, 2, 2048)
    pygame.mixer.music.load("sounds/coin.WAV")
    pygame.mixer.music.play(0)