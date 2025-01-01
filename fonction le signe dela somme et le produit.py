while True:
 def  somme_produits(a,b):
  S=a+b
  P=a*b
  if S>0 and P>0:
      print(" somme est positif  et produits est positifes")
  elif S>0 and P<0:
      print(" la somme est positif le produits est négatife")
  elif S<0 and P>0:
      print("la somme est négatife le produits est positif")
  elif S<0 and P<0:
      print("la somme est négatife le produits est négtife")
 n=int(input("donner le nombre permier \n"))
 m=int(input("donner le nombre permier \n"))
 somme_produits(m,n)
