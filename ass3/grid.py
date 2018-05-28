from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

GRID_SIZE = 10

class Grid:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.points = []
        glutInit()
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(sizeX * GRID_SIZE, sizeY * GRID_SIZE)
        glutCreateWindow("Raster".encode("ascii"))
        glOrtho(0, sizeX * GRID_SIZE, sizeY * GRID_SIZE, 0, -1, 1)
        glutDisplayFunc(self.display)
        glutKeyboardFunc(self.end)

    def addPoint(self, x, y, c = 1):
        if 0 <= x < self.sizeX and 0 <= y < self.sizeY:
            x = round(x)
            y = round(y)
            self.points.append((x, y, c))
        
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT) 
        for i in self.points:
            x, y, c = i
            if type(c) == tuple:
                glColor(*c)
            else:
                glColor(c, c, c)
            glBegin(GL_POLYGON)
            glVertex(x * GRID_SIZE, y * GRID_SIZE)
            glVertex((x + 1) * GRID_SIZE, y * GRID_SIZE)
            glVertex((x + 1) * GRID_SIZE, (y + 1) * GRID_SIZE)
            glVertex(x * GRID_SIZE, (y + 1) * GRID_SIZE)
            glEnd()
        glColor(.5, .5, .5)
        glBegin(GL_LINES)
        for i in range(1, self.sizeX):
            glVertex(i * GRID_SIZE, 0)
            glVertex(i * GRID_SIZE, self.sizeY * GRID_SIZE)
        for i in range(1, self.sizeY):
            glVertex(0, i * GRID_SIZE)
            glVertex(self.sizeX * GRID_SIZE, i * GRID_SIZE)
        glEnd()
        glFlush()

    def rasterline(self, x1, y1, x2, y2):
        #uses bresenham algorithm to determine which pixels to choose for line
        #inspiration for application of algorithm: https://www.youtube.com/watch?v=zytBpLlSHms
        
        dx = x2 - x1
        dy = y2 - y1
        sx = -1 if dx < 0 else 1                            #check which of x's is higher than other (necessary to know for while loop)
        sy = -1 if dy < 0 else 1

        if abs(dy) < abs(dx):                               #if in first octant
            slope = dy / dx
            pitch = y1 - slope * x1

            #for all x's between x1 and x2, calculate y value
            while (x1 != x2):                               #forloop in range x1,x2 doesn't work, maybe bc potential order  
                self.addPoint(x1, round(slope*x1+pitch))    
                x1 += sx                                    #will decrease if x1 higher than x2, for correct 'direction'

        else:                                               #if in other octants
            slope = dx / dy
            pitch = x1 - slope * y1

            while (y1 != y2):
                self.addPoint(round(slope*y1+pitch), y1)
                y1 += sy
          

    def end(self, key, x, y):
        exit()

    def draw(self):
        glutMainLoop()
