from math import *
d=0.00000001
eq=input("put in a function: ")
x=int(input("what is your first guess? "))
y=10000000
#while (y-x)<0.000001 and (y-x)>-0.000001:
y=x
deriv=(eval(eq(x+d)))
print(deriv)
