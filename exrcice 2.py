def remplir(T,n):
    for i in range (n):
        print("donner l’élemeny",i+1)
        y=int(input())
        T.append(y)
def afficher (T,n):
    for i in range(n):
        print(T[i])
D=[]
remplir(D,int(input("donner le inc=duce de tableaux")))
#afficher(D,len(D))
print(D)
