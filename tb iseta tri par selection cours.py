def remplir (T,n):
    for i in range (n):
        print(" donner un élément ",i+1)
        l=int(input())
        T.append(l)
def tri_selection(T,n):
    for i in range (n):
        mina=i
        for j in range (i+1,n):
            if T[j]<T[mina]:
                mina = j
                T[i],T[mina]=T[mina],T[i]
Q=[]
nn=int(input("donner un undice"))
remplir(Q,nn)
tri_selection(Q,nn)
print(Q)


    
