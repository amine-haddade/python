#ofnction  remplir et afficher et calculer la somme et produit du tableaux#

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
ci=0
cp=0
for i in range (len(R)):
    s=s+R[i]
    p=p*R[i]
    if R
    [i]%2==0:
        print(R[i],"est pairs")
        cp=cp+1
    else :
        print(R[i],"est impairs")
        ci=ci+1
print("la somme des élement du tableaux",s)
print("le produit de élement de tableaux",p)
print("la moyen de élement du tableaux",s/len(R))
print("nombre desélément impairs c’est ",ci)
print("nombre desélément pairs c’est ",cp)
