from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import projection as proj


class Cube():
    # [x,y,z]
    vertices = [[-1, -1, -1],
               [1, -1, -1],
               [1, 1, -1],
               [-1, 1, -1],
               [-1, -1, 1],
               [1, -1, 1],
               [1, 1, 1],
               [-1, 1, 1]]
    
    edges = ((0,1),
             (0,3),
             (0,4),
             (2,1),
             (2,3),
             (2,6),
             (5,1),
             (5,4),
             (5,6),
             (7,3),
             (7,4),
             (7,6))

    #for quads
    surfaces = ((0,1,2,3),
                (1,5,6,2),
                (5,4,7,6),
                (4,0,3,7),
                (3,2,6,7),
                (4,5,1,0))

    def __init__(self, window, x, y, z, scale, rotation, color):
        self.window = window
        self.x = x
        self.y = y
        self.z = z
        self.scale = scale
        self.rotation = rotation
        self.color = color

    #returns coordinates of vertices, after calculating new coordinates, after scale is applied (and moved 'back' after scaling)
    def vertexCoordinates(self):
        coordinates = []
        for vertex in self.vertices:
            new_x = vertex[0] * self.scale * 0.5 + self.x
            new_y = vertex[1] * self.scale * 0.5 + self.y
            new_z = vertex[2] * self.scale * 0.5 + self.z
            coordinates.append((new_x, new_y, new_z))
        return coordinates
    
    def update(self, dt):
        if self.window.move:
            self.rotation -= 100 * dt

    def draw(self):
        isometricCoordinates = proj.isometricProjection(self.vertexCoordinates(), self.rotation, self.window)

        glColor(self.color)

        #surfaces (polygons)
        glBegin(GL_QUADS)
        for surface in self.surfaces:
            for vertex in surface:
                glVertex(isometricCoordinates[vertex])
        glEnd()

        #lines along edges
        glColor(1, 1, 1)
        glBegin(GL_LINES)
        for edge in self.edges:
            glVertex(isometricCoordinates[edge[0]])
            glVertex(isometricCoordinates[edge[1]])
        glEnd()


class shootingStar:
    def __init__(self,window, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def update(self, dt):
        pass

    def getCurveCoordinates(self):
        return_list = []
        for t in range(0, 10, 1):
            t *= 0.1
            x = (1 - t) ** 2 * self.p1[0] + 2 * (1 - t) * t * self.p2[0] + t ** 2 * self.p3[0]
            y = (1 - t) ** 2 * self.p1[1] + 2 * (1 - t) * t * self.p2[1] + t ** 2 * self.p3[1]
            return_list.append((int(x), int(y)))
        return return_list

    def draw(self):
        glColor(1, 1, 1)

        #curve
        glBegin(GL_LINE_STRIP)
        for coordinate in self.getCurveCoordinates():
            glVertex(coordinate)
        glEnd()

        #star
        glBegin(GL_LINES)
        glVertex(self.p3[0], self.p3[1]-10)
        glVertex(self.p3[0], self.p3[1]+10)
        glVertex(self.p3[0]-10, self.p3[1])
        glVertex(self.p3[0]+10, self.p3[1])
        glVertex(self.p3[0]-5, self.p3[1]-5)
        glVertex(self.p3[0]+5, self.p3[1]+5)
        glVertex(self.p3[0]-5, self.p3[1]+5)
        glVertex(self.p3[0]+5, self.p3[1]-5)
        glEnd()

