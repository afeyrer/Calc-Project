from math import *
eq=input("This program will estimate the length of a curve. Put in a function: ")
xs=float(input("what is the leftmost x value? "))
xf=float(input("what is the rightmost x value? "))
d=(xf-xs)/10000
l=0
while xs<xf:
    x=xs
    y1=(eval(eq))
    xs=xs+d
    x=xs
    y2=(eval(eq))
    l=l+((y2-y1)**2+d**2)**(0.5)
print (round(l, 4))

