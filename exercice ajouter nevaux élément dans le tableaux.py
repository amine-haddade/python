#program ajouter un nombre de tableaux
def lir (T,n):
    for i in range (n):
        print(" veuillez saisir élément",i+1)
        e=int(input())
        T.append(e)
R=[]
n=int(input("entre le dimonsion de tablaux\n"))
lir(R,n)
print(R)
print(" donner neveau élement \n")
x=int(input())
k=int(input("veuillez saisir la position dans le tableaux\n"))
while k>len(R):
    print("Veuillez entrer un emplacement existant dans le tableau")
    k=int(input("veuillez saisir la position dans le tableaux\n"))
for i in range(1,n+1):
    if k-1==i:
        R.insert(k-1,x)

print(R)


