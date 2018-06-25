from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

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




class IsometricProjection:

    #multiplies a matrix with a vector
    def multMatrixVector(self, matrix, vector):
        return_matrix = [0] * len(matrix)
        if len(matrix[0]) == len(vector):
            for i in range (0, len(matrix)):
                for j in range(0, len(vector)):
                    return_matrix[i] += matrix[i][j] * vector[j]
        return return_matrix

    #multipies a matrix with a matrix
    def multMatrixMatrix(self, matrix_one, matrix_two):
        return_matrix = []
        for i in range (0, len(matrix_one)):
            return_matrix.append([])
            for j in range (0, len(matrix_two[0])):
                return_matrix[i].append(0)

        if len(matrix_one[0]) == len(matrix_two):
            for h in range (0, len(matrix_one[0])):
                for i in range (0, len(matrix_one)):
                    value = 0
                    for j in range(0, len(matrix_one[0])):
                        value += matrix_one[i][j] * matrix_two[j][h]
                    return_matrix[i][h] = value
            return return_matrix



