print(" donner un nombre ")
n=int(input())
cp1=0
cp2=0
cp3=0
for i in range(1,n):
    x=int(input(" doner " ))
    if (x>0):    
      print(x,"st plus positif")
      cp1==cp1+1
    elif (x<0):
      print(x,"estnégatif")
      cp2==cp2+1
    else :
       print(x, "est nul")
       cp3==cp3+1
print(cp1)
print(cp2)
print(cp3)
