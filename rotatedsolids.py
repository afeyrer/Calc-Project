from math import *
eq=input("This program will estimate the volume of a function rotated around the x axis or the y axis. Put in a function: ")
k=input("x axis or y axis (type x or y) ")
xs=float(input("what is the first limit of integration? "))
xf=float(input("what is the second limit of integration? "))
d=(xf-xs)/10000
nt=0
nta=0
x=xs
x1=xs
y1=eval(eq)
x=xf
yf=eval(eq)
while xs<=xf and k=="x":
    x=xs
    nt=nt+(eval(eq))**2*d*pi
    xs=xs+d
while xs<xf and k=="y":
    x=xs
    nta=nta+(eval(eq))*2*pi*xs*d
    xs=xs+d
if k=="x":
    nt= (nt*2-(y1)**2*d*pi-(yf)**2*d*pi)/2
    print("around the x: " + str(round(nt, 4)))
if k=="y":
    nta= (nta*2-(y1)*2*d*pi*x1-(yf)*2*d*pi*xf)/2
    print("around the y: " + str(round(nta, 4)))
    
