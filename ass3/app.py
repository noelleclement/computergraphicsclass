from grid import *

g = Grid(30, 30)

g.rasterline(2, 2, 16, 8)       #left top to middle middletop
g.rasterline(8, 21, 29, 1)      #left bottom to right top
g.rasterline(16, 10, 2, 16)     #middle top to left middle > order doesnt matter
g.rasterline(25, 8, 27, 22)     #right high to right low


g.draw()