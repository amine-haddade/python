def parfait (n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    if s==n:
        return 1
    else:
        return 0
print(" donner un nombre")
n=int(input())
for i in range (1,n+1):
    if parfait(i)==1:
      print(i)
print(parfait(6))
    
