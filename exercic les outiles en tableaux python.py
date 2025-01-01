def remplir(T,n):
    for i in range (n):
        print(" donner élément",i+1)
        n=int(input())
        T.append(n)
t=[]
n=int(input("donner les dimonsion de tableaux \n"))
remplir(t,n)
print(t)
x=int(input("veuillez saisir un éùément pour chercher "))
if x in t:
    print(" l'élément exsiste dans le tableaux")
    y=int(input(" donner neveau élément dans le tableaux "))
    indice=t.index(x)
    t[indice]=y
    print(t)
else :
    print("élément n'exsiste pas dands le tableaux\n")
    print(" entrer  postion dans tableaux por ajouter un l'élément dans tableaux\n")
    b = int(input())
    t.insert( b-1 , x)
    print("le tableaux mis à jour:\n",t)
    






