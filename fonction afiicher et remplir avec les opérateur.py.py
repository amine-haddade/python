def lir (T,n):
    for i in range(1,n+1):
        print("donner le élément",i,"dans le tableaux")
        c=int(input())
        T.append(c)

def afficher (T, n):
    for i in range(n):
        print(T[i])
        
R=[]
b=int(input("donner indice de tableaux\n"))
lir(R,b) 
#afficher(R, len(R))
print(R)
s=0
p=1
for i in range (len(R)):
    s=s+R[i]
    p=p*R[i]
print("la somme des élement du tableaux",s)
print("le produit de élement de tableaux",p)
print("la moyen de élement du tableaux",s/len(R))


