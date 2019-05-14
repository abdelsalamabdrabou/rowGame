from initialize import *
from collision import *
from final import *
from generate import *
sound()

# boat.py consists of the classes of Model and Transformation
# initialize consists of the Camera and Light settings
# settings.py consists of variables and constants we need it

# To make the game runs in FPS (Frame per second)
# we control it by FPS in settings.py
def idle(v):
    global previousTime, dt
    # calling display function according to number of FPS
    display()
    # calculate time to use it in motion according the time of calling display()
    # dt = the new calling - past calling
    currentTime = glutGet(GLUT_ELAPSED_TIME)
    dt = (currentTime - previousTime) / 1000 # 1000 converts from msec to sec
    previousTime = currentTime # storing the last time to use it in new calculation
    glutTimerFunc(1000//FPS, idle, 1)

def physicalMotion(key, x, y):
    global pos, vel, theta, acc, posz
    global dt
    global crashed, playerWin

    if (crashed != True) or (playerWin == False):
       if key == GLUT_KEY_RIGHT:
           acc[0] = 0.05 # the rating of increasing the acceleration
           theta -= 0.5 # the angle of deviation
       elif key == GLUT_KEY_LEFT:
            acc[0] = -0.05 # the opposite accelertion (-ve)
            theta += 0.5

       posz -= 0.5

       acc += vel * 0.1 # new acceleration = the past acc + velocity
       vel += acc * dt # velocity = init velocity + acceleration * time (newton)
       pos += vel + 0.5 * acc * dt * dt # pos = init pos + vel * ... (newton)


def display():
    global cubeA, posz
    global dt, theta
    global crashed, score, playerWin
    global objects, rocks, coins, collisionCoins

    myInit()
    # We put LookAt here for changing the camera position with the motion of boat (posz)
    gluLookAt(0, 3.5, 5+posz , 0, 0, posz, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Final destination
    drawFinalMark()

    ground()
    rocksGen()

    ###### Creat Model ######
    boat = Model()
    boat.creatModel("boat")

    ###### Boat Transformations ######
    boat.transforms().translate(pos[0], -1, 1.2+posz)
    boat.transforms().rotate(theta,0,1,0)
    boat.transforms().scale(0.3, 0.3, 0.3)
    boat.flushModel()
    glLoadIdentity()

    ###### Construct cube for collision #####
    # Cube affected by boat transformation
    # Center of cube (pos[0], -1, 1.2+posz)

    boat.transforms().translate(pos[0], -1, 1.2 + posz)
    boat.transforms().rotate(theta, 0, 1, 0)
    glScale(cubeWidth, 0, cubeLength)
    glColor4f(0, 0, 0, 0)
    glutSolidCube(1)
    glLoadIdentity()

    # points of cube center in xz-plane
    cubeA[0] = pos[0]
    cubeA[2] = 1.2 + posz

    ##### Final collision #####
    if testFinal(posz):
        playerWin = True

    ##### Show the score #####
    if playerWin:
        playerWon(score)

    ##### Coin collision #####
    if coinCollision(cubeWidth , cubeLength , outerR*0.3, coins.xPos(), coins.zPos()):
        score = score + 1
        soundCoin()

    ##### Rock collision #####
    if rockCollision(cubeWidth, cubeLength, rockRadius, rocks.xPos(), rocks.zPos()):
        crashed = True

    ##### Terrain collision #####
    if collWithRightTerrain(pos[0]):
        pos[0] = pos[0] - 0.5  # to make back for boat after collsion with terrain

    if collWithLeftTerrain(pos[0]):
        pos[0] = pos[0] + 0.5   # to make back for boat after collsion with terrain

    ##### Game over #####
    if crashed:
        WINDOW_WIDTH, WINDOW_HEIGHT = VIEWPORT

        glClearColor(0.0, 0.0, 0.0, 0.0)  # make the black color on background
        glClear(GL_COLOR_BUFFER_BIT)  # clear the buffer which the seen of boat

        glMatrixMode(GL_PROJECTION)  # make the new seen
        glLoadIdentity()  # clear the transformer matrix
        glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1)  # l,r,b,t,n,f

        glMatrixMode(GL_MODELVIEW)

        drawText("Game Over", 50, 400)  # draw  "game over"
        drawText("SCORE:", 50, 200)  # draw "score"
        drawText(str(score), 650, 200)  # draw score


    ###### Construct the track ######
    # Right side

    # Translate all and moving with camera along -z
    glTranslate(xTrackCenter, -1, 1.5+posz)
    glScale(1.5, 1.2, 1)
    for i in range(0, 30):
        glColor3f(0.557,0.941,0.278)
        glutSolidSphere(trackRadius, 10, 20)
        glTranslate(0, 0, -1)

    glLoadIdentity()

    # Left side
    glTranslate(-xTrackCenter, -1, 1.5+posz)
    glScale(1.5, 1.2, 1)
    for i in range(0, 30):
        glColor3f(0.557, 0.941, 0.278)
        glutSolidSphere(trackRadius, 10, 20)
        glTranslate(0, 0, -1)

    glLoadIdentity()

    glutSwapBuffers()


glutInit()
glutInitWindowSize(800,600)
glutCreateWindow(b"ROW ROW")
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
initLight()
myInit()
glutDisplayFunc(display)
glutTimerFunc(1000//FPS, idle, 1)
glutSpecialFunc(physicalMotion)
glutMainLoop()