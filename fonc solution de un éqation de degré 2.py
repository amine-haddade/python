import math

def éq(a,b,c):
    D=b**2-4*a*c
    return D


def eq(a,b,c):
    D=b**2-4*a*c
    
    if D>0:
        
        s1=(-b - math.sqrt(D)) / (2*a)
        s2=(-b - math.sqrt(D)) / (2*a) 
        print(s1,"et",s2)
        
    if D==0:
        
        s3=(-b/2*a)
        print(s3)
        
    if D<0:
        print("le equation null")

            
a=int(input("donner a"))

b=int(input("donner b"))

c=int(input("donner c"))

print(éq(a,b,c))

eq(a,b,c)
"""import math

def éq(a, b, c):
    D = b**2 - 4*a*c
    return D

def eq(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        s1 = (-b - math.sqrt(D)) / (2*a)
        s2 = (-b + math.sqrt(D)) / (2*a)
        print("Les solutions sont", s1, "et", s2)
    elif D == 0:
        s3 = -b / (2*a)
        print("La solution unique est", s3)
    else:
        print("L'équation n'a pas de solution réelle.")

a = int(input("Donner a: "))
b = int(input("Donner b: "))
c = int(input("Donner c: "))

print("Discriminant D =", éq(a, b, c))
eq(a, b, c)"""
