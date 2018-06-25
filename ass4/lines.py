from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math


'''
Workings of program:
- a window is created (with certain characteristics like width and height)
- a cube is created (with location and scale)
- rotation is given
- new points for isometric projection are calculated
    - for both horizontal and vertical transformations a matrix multiplication is done 
    - the combo of that is applied to all coordinates of the cube
    - lines are 'drawn' (given to OpenGL) between said coordinates
- the complete drawing is drawn on screen
'''


class Lines:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.lines = []
        glutInit()
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(sizeX, sizeY)
        glutCreateWindow("Lines".encode("ascii"))
        glOrtho(0, sizeX, sizeY, 0, -1, 1)
        glutDisplayFunc(self.display)
        glutKeyboardFunc(self.end)

    def addLine(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        if 0 <= x1 < self.sizeX and \
           0 <= y1 < self.sizeY and \
           0 <= x2 < self.sizeX and \
           0 <= y1 < self.sizeY:
            self.lines.append((x1, y1, x2, y2))

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor(1, 1, 1)
        glBegin(GL_LINES)
        for i in self.lines:
            x1, y1, x2, y2 = i
            glVertex(x1, y1)
            glVertex(x2, y2)
        glEnd()
        glFlush()

    def end(self, key, x, y):
        exit()

    def draw(self):
        glutMainLoop()


#wrap for matrix functions
class Matrix:
    #multiplies matrix with vector
    def multiplyVector(matrix, vector): 
        result = [0] * len(matrix)
        if len(matrix[0]) == len(vector):
            for i in range(0,len(matrix)):
                for j in range(len(vector)):
                    result[i] += matrix[i][j] * vector[j]
            return result

    #multiplies 2 matrices
    def multiplyMatrices(matrix1, matrix2): 
        result = []

        for i in range (0, len(matrix1)):
            result.append([])
            for j in range (0, len(matrix1)):
                result[i].append(0)


        if len(matrix1[0]) == len(matrix2):
            for h in range (0, len(matrix2)):
                for i in range (0, len(matrix1)):
                    value = 0
                    for j in range(0, len(matrix2)):
                        value += matrix1[i][j] * matrix2[j][h]
                    result[i][h] = value
            return result    



#wrap for isometric projection functions
class IsometricProjection:
    #calculation of new coordinates for isometric projection
    def isometricise(coordinateList, rotation):
        isometricCoordinates = []
        alpha = math.asin(math.tan(math.radians(30))) #vertical rotation
        beta = math.radians(45 + rotation) #horizontal rotation
        
        matrixHorizontalRotation = ((math.cos(beta),0, math.sin(beta) * -1),
                (0,1,0),
                (math.sin(beta),0,math.cos(beta)))

        matrixVerticalRotation = ((1,0,0),
            (0,math.cos(alpha),math.sin(alpha)),
            (0,math.sin(alpha) * -1, math.cos(alpha)))

        combinedMatrix = Matrix.multiplyMatrices(matrixVerticalRotation, matrixHorizontalRotation)

        for coordinate in coordinateList:
            isometricCoordinate = Matrix.multiplyVector(combinedMatrix, coordinate)
            isometricCoordinates.append((isometricCoordinate[0]+windowWidth/2, isometricCoordinate[1]+windowHeight/2)) 

        return isometricCoordinates

    #for all given edges (in this case, of cube), create the line
    def draw(isometricCoordinates, edges):
        for edge in edges:
            l.addLine(isometricCoordinates[edge[0]], isometricCoordinates[edge[1]])



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

    edges = ((0, 1),
            (1, 2),
            (2, 3),
            (0, 3),
            (0, 4),
            (1, 5),
            (2, 6),
            (3, 7),
            (4, 5),
            (5, 6),
            (6, 7),
            (4, 7))

    def __init__(self, x, y, z, scale):
        self.x = x
        self.y = y
        self.z = z
        self.scale = scale

    #calculates new coordinates of vertices, after scale is applied (and moved 'back')
    def vertexCoordinates(self):
        coordinates = []
        for vertex in self.vertices:
            new_x = vertex[0] * self.scale * 0.5 + self.x
            new_y = vertex[1] * self.scale * 0.5 + self.y
            new_z = vertex[2] * self.scale * 0.5 + self.z
            coordinates.append((new_x, new_y, new_z))
        return coordinates

    def returnEdges(self):
        return self.edges




windowWidth = 640
windowHeight = 480

l = Lines(windowWidth, windowHeight)

cube = Cube(0, 0, 0, 200) #creates cube

rotation = 0 #changes rotation

points = IsometricProjection.isometricise(cube.vertexCoordinates(), rotation)

IsometricProjection.draw(points, cube.returnEdges())
l.draw()




