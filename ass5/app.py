from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time

from shapes import *

'''
for assignment:


This application shows a square Earth and Moon, and a shooting star in a black galaxy. 
By pressing the spacebar the animation can be stopped or started (depending on the state).
By pressing the escape key, the application will be closed. 


gebruikte technieken
• polygonen (quads voor cube)
• 3D-vormen (cubes)
• animatie (rotatie)
• gebruikersinteractie (spatiebalk stopt/start animatie)
• 3D transformaties (rotatie in 3d)
• perspectief (isometrische projectie + 3d)
• krommen (shootingstar)
'''

class Window():
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.attributes = []
        self.oldTime = time.time()
        self.move = True
        glutInit()
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(sizeX, sizeY)
        glutCreateWindow("Galaxy".encode("ascii"))
        glOrtho(0, sizeX, sizeY, 0, -1, 1)
        glutDisplayFunc(self.display)
        glutKeyboardFunc(self.keyboard)
        glutTimerFunc(50, self.update, 1)

        #should i attempt texture mapping, this was given as an example, dont forget to put timerfunc after
        '''
        data=pyglet.image.load("redbrick.png").get_data()       #dont forget to import pyglet
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, (image_width), (image_height), 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
        '''
        
    
    def update(self, value):
        newTime = time.time()
        dt = newTime - self.oldTime
        self.oldTime = newTime

        for attribute in self.attributes:
            attribute.update(dt)

        glutTimerFunc(50, self.update, 1)
    

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)

        for attribute in self.attributes:
            attribute.draw()

        glFlush()
        glutPostRedisplay()

    def keyboard(self, key, x, y):
        if key == b"\x1b": # escape
            exit()
        if key == b"\x20": #  spacebar  
            self.move = not self.move

    def draw(self):
        glutMainLoop()


windowWidth = 640
windowHeight = 480
scale = 200
rotation = 30

window = Window(windowWidth, windowHeight)
cube1 = Cube(window, 0, 0, 0, scale, rotation, (0.1, 0.5, 1))
cube2 = Cube(window, 200, -100, 0, 50, 10, (0.5,0.5,0.5))
shootingStar = shootingStar(window, (30, 100), (70, 50), (130, 30)) #(-100, -100, 100), (-50, -100, 100), (0, -100, 100))
window.attributes.append(cube1)
window.attributes.append(cube2)
window.attributes.append(shootingStar)


window.draw()

