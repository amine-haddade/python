def multi(n):
 for i in range(1,11):
    print(n,"*",i,"=",n*i)
  
while True:
  n=int(input("donner le nombre "))
  if n>0:
   break

print(multi(n))