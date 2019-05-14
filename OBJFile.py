#[MIT license:]
#
# Copyright (c) 2004  Dave Pape    
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import string
from OpenGL.GL import *
from Texture2D import *


class OBJFace:
    def __init__(self, vertices, normals, texcoords, obj):
        self.vertices = vertices
        self.normals = normals
        self.texcoords = texcoords
        self.obj = obj
    def draw(self):
        glBegin(GL_POLYGON)
        for i in range(0, len(self.vertices)):
            if self.normals[i] > 0:
                glNormal3fv(self.obj.normals[self.normals[i] - 1])
            if self.texcoords[i] > 0:
                glTexCoord2fv(self.obj.texcoords[self.texcoords[i] - 1])
            glVertex3fv(self.obj.vertices[self.vertices[i] - 1])
        glEnd()

class OBJUseMtl:
    def __init__(self, mtl):
        self.material = mtl
    def draw(self):
        if self.material.has_key('Ka'):
            glMaterialfv(GL_FRONT, GL_AMBIENT, self.material['Ka'])
        else:
            glMaterialfv(GL_FRONT, GL_AMBIENT, [0, 0, 0, 0])
        if self.material.has_key('Kd'):
            glMaterialfv(GL_FRONT, GL_DIFFUSE, self.material['Kd'])
        else:
            glMaterialfv(GL_FRONT, GL_DIFFUSE, [0, 0, 0, 0])
        if self.material.has_key('Ks'):
            glMaterialfv(GL_FRONT, GL_SPECULAR, self.material['Ks'])
        else:
            glMaterialfv(GL_FRONT, GL_SPECULAR, [0, 0, 0, 0])
        if self.material.has_key('Ns'):
            glMaterialf(GL_FRONT, GL_SHININESS, self.material['Ns'])
        if self.material.has_key('map_Kd'):
            self.material['map_Kd'].apply()
        else:
            glDisable(GL_TEXTURE_2D)

class OBJFile:
    def __init__(self, filename):
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.materials = {}
        self.commands = []
        file = open(filename, "r")
        lines = file.readlines()
        for line in lines:
            values = string.split(line)
            if len(values) < 1:
                continue
            if values[0] == 'v':
                x = string.atof(values[1])
                y = string.atof(values[2])
                z = string.atof(values[3])
                self.vertices.append([x,y,z])
            elif values[0] == 'vn':
                x = string.atof(values[1])
                y = string.atof(values[2])
                z = string.atof(values[3])
                self.normals.append([x,y,z])
            elif values[0] == 'vt':
                s = string.atof(values[1])
                t = string.atof(values[2])
                self.texcoords.append([s,t])
            elif values[0] == 'mtllib':
                self.loadMtllib(values[1])
            elif values[0] == 'f':
                face = []
                texcoords = []
                norms = []
                for v in values[1:]:
                    w = string.split(v,'/')
                    face.append(string.atoi(w[0]))
                    if len(w) >= 2 and len(w[1]) > 0:
                        texcoords.append(string.atoi(w[1]))
                    else:
                        texcoords.append(0)
                    if len(w) >= 3 and len(w[2]) > 0:
                        norms.append(string.atoi(w[2]))
                    else:
                        norms.append(0)
                self.commands.append(OBJFace(face,norms,texcoords,self))
            elif values[0] == 'usemtl':
                if self.materials.has_key(values[1]):
                    self.commands.append(OBJUseMtl(self.materials[values[1]]))
                else:
                    print 'Warning: %s trying to use unknown material %s' % (filename, values[1])

    def loadMtllib(self, filename):
        for line in open(filename, "r").readlines():
            values = string.split(line)
            if len(values) < 1:
                continue
            if values[0] == 'newmtl':
                mtl = {}
                self.materials[values[1]] = mtl
            elif values[0] == 'Ka':
                r = string.atof(values[1])
                g = string.atof(values[2])
                b = string.atof(values[3])
                mtl['Ka'] = [ r, g, b ]
            elif values[0] == 'Kd':
                r = string.atof(values[1])
                g = string.atof(values[2])
                b = string.atof(values[3])
                mtl['Kd'] = [ r, g, b ]
            elif values[0] == 'Ks':
                r = string.atof(values[1])
                g = string.atof(values[2])
                b = string.atof(values[3])
                mtl['Ks'] = [ r, g, b ]
            elif values[0] == 'Ns':
                n = string.atof(values[1])
                mtl['Ns'] = n
            elif values[0] == 'map_Kd':
                mtl['map_Kd'] = Texture2D(values[1])

    def draw(self):
        if not hasattr(self,'displayList'):
            self.displayList = glGenLists(1)
            glNewList(self.displayList, GL_COMPILE)
            for c in self.commands:
                c.draw()
            glDisable(GL_TEXTURE_2D)
            glEndList()
        glCallList(self.displayList)
