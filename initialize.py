from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from settings import *

def initLight():
    glLightfv(GL_LIGHT0, GL_POSITION, (-40, 200, 100, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

def myInit():
    glEnable(GL_BLEND)
    glMatrixMode(GL_PROJECTION)
    width, height = VIEWPORT
    glLoadIdentity()
    gluPerspective(50, width / float(height), 1, 100.0)
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

def ground():

    glBegin(GL_POLYGON)
    for vertex in groundVertices1:
        glColor3f(0, 0.5, 0.5)
        glVertex3fv(vertex)
    glEnd()

    glBegin(GL_POLYGON)
    for vertex in groundVertices2:
        glColor3f(0.859, 0.584, 0.263)
        glVertex3fv(vertex)
    glEnd()

    glBegin(GL_POLYGON)
    for vertex in groundVertices3:
        glColor3f(0.859, 0.584, 0.263)
        glVertex3fv(vertex)
    glEnd()

    glLoadIdentity()


def drawText(string, x, y):
    glLineWidth(4)
    glColor(1, 1, 0)  # Yellow Color
    glLoadIdentity()  # remove the previous transformations
    glTranslate(x, y, 0)
    glScale(1, 1, 1)
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)