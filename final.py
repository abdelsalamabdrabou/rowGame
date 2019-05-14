from initialize import *

def drawFinalMark():
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(-3, -0.9, -126)
    glVertex(3, -0.9, -126)
    glVertex(3, -0.9, -128)
    glVertex(-3, -0.9, -128)
    glEnd()

def testFinal(z):
    if z <= -126:
        return True

def playerWon(score):
    WINDOW_WIDTH ,WINDOW_HEIGHT = VIEWPORT

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)

    # New screen
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1)  # l,r,b,t,n,f

    glMatrixMode(GL_MODELVIEW)

    drawText("Bravo!", 50, 400)
    drawText("SCORE:", 50, 200)
    drawText(str(score), 650, 200)