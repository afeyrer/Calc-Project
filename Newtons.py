from math import *
d=0.00000001
eq=input("put in a function: ")
xs=int(input("what is your first guess? "))
xf=10000000
while (xf-xs)>d or (xf-xs)<-d:
    xf=xs
    x=xs
    y=(eval(eq))
    x=xs+d
    yup=(eval(eq))
    x=xs-d
    yd=(eval(eq))
    deriv=(yup-yd)/(2*d)
    xs=xs-(y/deriv)
    print(xs)
