#Noëlle Clement
#computer graphics assignment 2


#notes for whole assignment:
    #rgb cmy sl and alpha all can have values between 0 and 1 (so often conversion isn't necessary in calculations)
    #h can have a value between 0 and 360
    #throughout whole assignment I have used the most basic means of calculating and coding the functions
    #bc of ^ comments weren't really necessary, since it's mainly implementing the formulas
    #formulas from RapidTables


#RGBtoCMY(R, G, B)
def RGBtoCMY(r, g, b):
    return (1-r), (1-g), (1-b) 



#CMYtoRGB(C, M, Y) cyaan magenta yellow
def CMYtoRGB(c, m, y):
    return (1-c), (1-m), (1-y)



#RGBtoHSL(R, G, B)
#rgb already 0-1 so no conversion needed
def RGBtoHSL(r,g,b):
    cMax = max(r,g,b)
    cMin = min(r,g,b)
    cDelta = cMax - cMin
    l = (cMax+cMin)/2

    if (cDelta == 0):
        h = 0
        s = 0
    elif (cMax == r):
        h = 60 * (((g-b)/cDelta)%6)
        s = cDelta/(2-abs(2*l-1))
    elif (cMax == g):
        h = 60 * (((b-r)/cDelta)+2)
        s = cDelta/(2-abs(2*l-1))
    elif (cMax == b):
        h = 60 * (((r-g)/cDelta)+4)
        s = cDelta/(2-abs(2*l-1))
    else:
        print ('wrong input in RGBtoHSL')

    return h, s, l
            


#HSLtoRGB(H, S, L)
def HSLtoRGB(h,s,l):
    c = (1-abs(2*l-1)) * s
    x = c*(1-abs((h/60)%2 - 1))
    m = l-c/2

    if (h>=0 and h<60):
        r=c
        g=x
        b=0
    elif (h>=60 and h<120):
        r=x
        g=c
        b=0
    elif (h>=120 and h<180):
        r=0
        g=c
        b=x
    elif (h>=180 and h<240):
        r=0
        g=x
        b=c
    elif (h>=240 and h<300):
        r=x
        g=0
        b=c
    elif (h>=300 and h<360):
        r=c
        g=0
        b=x
    else:
        print ('wrong input in HSLtoRGB')

    return (r+m), (g+m), (b+m)



#transparency(R1, G1, B1, alpha1, R2, G2, B2) of a surface (r1, g1, b1, a1) on top of (r2, g2, b2, 1)
#(R,G,B)res = a(R,G,B)front + (1-a)(R,G,B)back > alpha of back 1, so in this function not necessary to use whole formula
def transparency(r1,g1,b1,a1,r2,g2,b2):
    r1 = a1*r1
    g1 = a1*g1
    b1 = a1*b1
    return (r1+r2), (g1+g2), (b1+b2)



print (RGBtoCMY(0.5,0.5,0.5))
print (CMYtoRGB(1,1,1))
print (RGBtoHSL(0,1,0.5))
print (HSLtoRGB(180.0, 0.5, 0.5))
print (transparency(0,1,1,0.5,1,0.75,0))
