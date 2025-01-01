def lir (T,n):
    for i in range(n):
        print("donner l’élément",i+1)
        u=int(input())
        T.append(u)
def afficher(T):
    n=len(T)
    for i in range(n):
        print(T[i])
