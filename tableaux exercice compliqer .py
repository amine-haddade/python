#Q1#
def remplir (T):
    for i in range (5):
        print(" donner un élément ",i+1)
        n=int(input())
        T.append(n)
#Q2#
def afficher  (T):
    for i in range (20):
        print(T[i])
#Q3#
def chercher (T):
    print(" veuillez entrer la valeur qui chercher en tableaux")
    o=int(input())
    tt= True
    if o in T:
        tt=True
        print(tt)
    else:
        tt= False
        print(tt)
    return tt
def trier (R):
          for i in range(1,len(R)):
                    cle=R[i]
                    j=i-1
                    while j>=0 and R[j]>cle:
                         R[j],R[j+1]=R[j+1],R[j]
                         j-=1


#Q4#
def ajouter (T):
    a=int(input("donner élément tu veux ajouter\n"))
    pp=int(input("position de neveau élément"))
    T.insert(pp-1,a)
#Q5#
def t_o(T,n):
    for i in range (1,n+1):
        print("donner élément",i)
        j=int(input())
        T.append(j)
  
    for j in range(1,n):
       if T[j-1]>T[j]:
           print("FAUX")
           break
           
       else :
            print("VRAI")
            break
print("Vous fournir notre service plusieur opérateur pour modify les tableau\n")
print("pour chercher dans une valeur du tableau taper  1",2*"\n","pour ajouter élément dans ce tableau taper 2 ",2*"\n","pour savoir si tableau est dans un order decroisent taper 3",2*"\n")
c=int(input())
Q=[]
match c :
    case 1:
        remplir(Q)
        chercher(Q)
        print(Q)
    case 2:
        remplir(Q)
        ajouter(Q)
        print(Q)
    case 3:
        b=int(input("donner la dimonsion du tableau\n"))
        t_o(Q,b)
        print(Q)
    case 4:
        remplir(Q)
        trier(Q)
        print(Q)
        






    



