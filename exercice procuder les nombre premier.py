def premier(N):
    estpremier =True
    for i in range(2,N//2):
        if (N%i==0):
            estpremier=False
    if  estpremier==True:
        print(N,"est premier")
    else:
        print(N,"est non premier")
n=int(input("donner un nombre\n"))
premier(n)
    

            
