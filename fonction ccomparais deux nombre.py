def MIN(a,b):
    if a>b:
        min=b
    else :
        min=a
    return min
def MAX (a,b):
    if a>b:
    
        max=a
    else :
        max=b
    return max   
n=int(input("donne le nombre 1"))
h=int(input("donner le nombre 2"))
print("la valeure minimal c`est",MIN(n,h))
print("la valeure maximal c`est",MAX(n,h))
