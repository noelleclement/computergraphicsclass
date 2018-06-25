#draws a projection of a cube that has been rotated 30degrees around the y-axis

'''
Hoekpunten: v1 = (−1, −1, −1), v2 = (1, −1, −1),
v3 = (1,1,−1), v4 = (−1,1,−1), v5 = (−1,−1,1),
v6 = (1,−1,1), v7 = (1,1,1), v8 = (−1,1,1).
Ribben: v1v2, v2v3, v3v4, v4v1, v1v5, v2v6, v3v7, v4v8, v5v6, v6v7, v7v8, v8v5.
'''

import numpy as np
from lines import * 


#matrix multiplication with vector
x = [[1,2,3,0],[4,5,6,0],[7,8,9,0],[0,0,0,0]]
y = [[1],[2],[3],[0]]

mx = np.matrix(x)
my = np.matrix(y)

print(mx)
print(my)
print(mx*my)


ortho = [[1,0,0,0],[0,1,0,0]]
mOrtho = np.matrix(ortho)
print(mOrtho)
print(mOrtho*mx)


iso = [(1/np.sqrt(2)), 0, (1/np.sqrt(2)), 0], [(1/np.sqrt(6)), np.sqrt((2/3)), -(1/np.sqrt(6)), 0]
mIso = np.matrix(iso)
print(mIso)
print(mIso*mx)


h1 = [-1,-1,-1]
h2 = [1,-1,-1]
h3 = [1,1,-1]
h4 = [-1,1,-1]
h5 = [-1,-1,1]
h6 = [1,-1,1]
h7 = [1,1,1]
h8 = [-1,1,1]

print(multMatrixVector(x,y))



'''
l = Lines(640,480)
l.addLine(h1,h2)
l.draw()
'''