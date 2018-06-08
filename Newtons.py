from math import *
d=0.00000001
eq=input("put in a function: ")
xs=int(input("what is your first guess? "))
y=10000000
#while (y-xs)<0.000001 and (y-xs)>-0.000001:
x=xs+d
yup=(eval(eq))
print (yup)
x=xs-d
yd=(eval(eq))
print (yd)
deriv=(yup-yd)/(2*d)
print(round(deriv, [9]))

