n=int(input("donne un nomnre de début ")) 
m=n
M=n
pox1=0
pox2=0
for i in range(1,6):
 n=int(input("donne un nomnre")) 
 if(n>m):
    print(" lavaleur maximale ",n)
    pox1=pox1+1
 elif(n<M):
    print(" lavaleur minimal ",n)
    pox2=pox2+1
print("le nombre de  valeur max",pox1)
print("le nombre de  valeur min",pox2)
