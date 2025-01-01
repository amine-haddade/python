#sérer exercice
#exercice 1
def lir(T,n):
    for i in range (n):
        print("donner le élément",i+1,"du tablaeux")
        f=int(input())
        T.append(f)
def afficher(T):
    n=len(T)
    for i in range(n):
        print(T[i])

o=[]
z=int(input("donner la dimonsion du tableaux\n"))
lir(o,z)
print(o)

A=[]
for i in range (z):
   A.append(o[i]*2)
print(A)


