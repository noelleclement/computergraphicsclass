#Noëlle Clement
#computer graphics assignment 2


#RGBtoCMY(R, G, B)
	#bc rgb can have values between 0 and 1 no need for conversion from 0-255 to 0-1 
	#k(black) = 1-max(r, g, b)
	#c = (1-r-k) / (1-k)
	#m = (1-g-k) / (1-k)
	#y = (1-b-k) / (1-k)

def RGBtoCMY(r, g, b):
    if (r == 0) and (g == 0) and (b == 0):
        #black
        return 0, 0, 0

    return (1-r), (1-g), (1-b) 



#CMYtoRGB(C, M, Y) cyaan (turkoois) magenta yellow
	#r = 255 x (1-c) x (1-k)
	#g = 255 x (1-m) x (1-k)
	#b = 255 x (1-y) x (1-k)


def CMYtoRGB(c, m, y):
    return (1-c), (1-m, (1-y)



#RGBtoHSL(R, G, B)



//HSLtoRGB(H, S, L)
//transparency(R1, G1, B1, alpha1, R2, G2, B2) of a surface (r1, g1, b1, a1) on top of (r2, g2, b2, 1)

//RGB CMY SL and alpha can have values between 0 and 1
//H can have value between 0-360 degrees



