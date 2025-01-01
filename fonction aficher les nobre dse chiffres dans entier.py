def chiffre (M):
    nbr = 0
    while M != 0:
        nbr = nbr + 1
        M=M // 10
    print(nbr)
    
n=int(input("donner un nombre\n"))
chiffre(n)
"""def chiffre(N):
    nbr = 0
    while N != 0:  # Change the condition to check if N is not equal to 0
        nbr = nbr + 1  # Use a single equal sign to assign the value
        N = N // 10
    print(nbr)

n = int(input("Donnez un nombre\n"))
chiffre(n)"""
