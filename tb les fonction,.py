#111
n=int(input("donner la dimension detableaux"))
T=[]
for i in range(n):
    print(" veuillez saisir element",i+1)
    e=int(input())
    T.append(e)
#222
print(T)
#333
print(" entrer élément et chercher si lement exsiste dans tableaux")
x=int(input())
if x in T:
    print("élément exsiste")
    print("donner un valeur pou la remplacer")
    d=int(input())
    a=T.index(x)
    T[a]=d
    print(T)
    
else :
    print(" n'existe pas")
    print("saisir position de élément dans un tableaux")
    y=int(input())
    T.insert(y-1,x)
    print(T)
    

