"""def lir (T,n):
    for i in range(n):
        print(" donner un nombre")
        c=int(input())
        T.append(c)
    return(T)
def inverse (T1,T2,n):
    for i in range(n):
        T2.append(T1(n-i))"""
    
a=[]
z=[]
print(" donner indice de tableaux")
b=int(input())
for i in range(1,b+1):
    print("donner élément",i)
    v=int(input())
    a.append(v)
print(a)
for ii in range (1,b+1):
    z.append(a[b-ii]) 
print(z)








