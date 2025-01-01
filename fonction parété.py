def parité(M,N):
    while M>N:
        print(" no tu doit entrer le nombre 2 structement supérieur le nombre 1\n")
        M=int(input("donner le nombre 1\n"))
        N=int(input("donner le nombre 2\n"))
    for i in range(M,N+1):
        if i%2==0:
            print(i)
M=int(input("donner le nombre 1\n"))
N=int(input("donner le nombre 2\n"))
parité(M,N)
