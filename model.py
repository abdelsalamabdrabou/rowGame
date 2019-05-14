from objloader import *

class Transforms:
    def translate(self, tx, ty, tz):
        glTranslate(tx, ty, tz)

    def rotate(self, angle, rx, ry, rz):
        glRotate(angle, rx, ry, rz)

    def scale(self, sx, sy, sz):
        glScale(sx, sy, sz)

class Model:
    def __init__(self):
        self.model = None

    def creatModel(self, objname):
        self.model = OBJ("objects/"+objname+".obj", swapyz=True)

    def flushModel(self):
        glCallList(self.model.gl_list)

    def transforms(self):
        return Transforms()

class Position:
    def __init__(self):
        self.x = []
        self.z = []

    def xPoint(self, x):
        self.x.append(x)

    def zPoint(self, z):
        self.z.append(z)

    def xPos(self):
        return self.x

    def zPos(self):
        return self.z