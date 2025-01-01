while True:
 def parété(A):
    if (A%2==0):
        p="paire"
    else:
        p="impaire"
    return p
 print("donner un nombre")
 n=int(input())
 print(" le nombre",parété(n))
