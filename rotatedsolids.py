from math import *
eq=input("This program will estimate the volume of a function rotated around the x axis or the y axis. Put in a function: ")
k=input("x axis or y axis (type x or y)")
xs=float(input("what is the first limit of integration? "))
xsa=xs
xf=float(input("what is the second limit of integration? "))
d=(xf-xs)/10000
nt=0
nta=0
while xs<xf and k=="x":
    x=xs
    nt=nt+(eval(eq))**2*d*pi
    xs=xs+d
while xsa<xf and k=="y":
    x=xsa
    nta=nta+(eval(eq))*2*pi*xsa*d
    xsa=xsa+d
if k=="x":
    print("around the x: " + str(round(nt, 4)))
if k=="y":
    print("around the y: " + str(round(nta, 4)))
    
