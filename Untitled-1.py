def lir (r,n):
    for i in range(n):
        print("donner élémet",i+1)
        b=int(input())
        r.append(b)
    return(r)
def somme(y,n):
    s=0
    for i in range(n):
        s=s+y[i]
    print(s)
def moyen(r,n):
    s=0
    for i in range(n):
        s=s+r[i]
    m=s/n
    print(m)
def nbr_moyen(r,n):
    s=0
    for i in range(n):
        s=s+r[i]
    m=s/n
    for i in range(n):
        if r[i]>=m:
            print(r[i])
def tri(r,n):
    for i in range(n):
        mina=i
        for j in range(i+1,n):
            if r[j]<r[mina]:
                mina=j
                r[i],r[mina]=r[mina],r[i]


r=[]
n=int(input("donner indice de tableau"))
print(lir(r,n))
tri(r,n)
print(r)
somme(r,n)
moyen(r,n)
nbr_moyen(r,n)


        