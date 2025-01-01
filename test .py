def premier (n):
    box=0
    for i in range(1,n+1):
       if n%i==0:
         box=box+1
    if box==2:
        print(n,"est premier")
    else :
        print(n,"est nom premier")
n=int(input(" donner le nombre qui doit tester "))
premier (n)