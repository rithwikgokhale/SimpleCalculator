#Python Script to solve quadratic equations and give the solutions

print ("Quadratic Equations: ax^2+bx+c = 0")
a = int(input("Enter the coefficients of a: "))
b = int(input("Enter the coefficients of b: "))
c = int(input("Enter the coefficients of c: "))

d = b**2-4*a*c # this is the discriminant for the entered quadratic equation

e = str(a)+("x^2+")+str(b)+("x+")+str(c) #This is the quadratic equation

from math import sqrt

if d < 0: #Applicable only if the discriminant is less than zero
    print ("The equation: "), e, ("has no real solution.")
elif d == 0:  #Applicable only if the discriminant is equal to zero
    x = (-b+sqrt(b**2-4*a*c))/2*a
    print ("The equation: "), e, ("has one solution. ")
    print ("Solution 1: "), x
else:  #Applicable only if the discriminant is greater than zero
    x1 = (-b+sqrt((b**2)-(4*(a*c))))/(2*a)
    x2 = (-b-sqrt((b**2)-(4*(a*c))))/(2*a)
    print ("The equation: "), e, ("has two solutions. ")
    print ("Solution 1: "), x1
    print ("Solution 2: "), x2

