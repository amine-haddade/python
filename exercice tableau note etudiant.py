               #<--------algorithmr lres étudiant admis------------>
def lir (T,n):
    for i in range(1,n+1):
        print(" donner la valeure de note ",i)
        n=float(input())
        T.append(n)
    return T
T1=[]
T=[]
print(" donner les nombre de étudiant")
n=int(input())
lir(T,n)
for note in T :
    if note >= 10:
        
        T1.append(note)
print(T1)
