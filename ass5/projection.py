import math


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

#calculation of new coordinates for isometric projection
def isometricProjection(coordinateList, rotation, window):
    isometricCoordinates = []
    alpha = math.asin(math.tan(math.radians(30))) #vertical rotation
    beta = math.radians(45 + rotation) #horizontal rotation
    
    matrixHorizontalRotation = ((math.cos(beta),0, math.sin(beta) * -1),
            (0,1,0),
            (math.sin(beta),0,math.cos(beta)))

    matrixVerticalRotation = ((1,0,0),
        (0,math.cos(alpha),math.sin(alpha)),
        (0,math.sin(alpha) * -1, math.cos(alpha)))

    combinedMatrix = multiplyMatrices(matrixVerticalRotation, matrixHorizontalRotation)

    for coordinate in coordinateList:
        isometricCoordinate = multiplyVector(combinedMatrix, coordinate)
        isometricCoordinates.append((isometricCoordinate[0]+window.sizeX/2, isometricCoordinate[1]+window.sizeY/2)) 

    return isometricCoordinates