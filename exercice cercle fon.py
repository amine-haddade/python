def daimtre(R):
    D=R**2
    return D
def péraimetre (R):
    P=2*3.14*R
    return P
def surface (R):
    S=R**2*3.14
    return S
r=float(input("donner la rayon"))
print(" le daimetre  ",daimtre(r))
print(" la surface ",surface(r))
print(" la péremtere ",péraimetre(r))
