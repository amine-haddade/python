print("1;tv:400$\n2;ordinateur:200$\n3;téléphone:200$\n4;portable:900$\n")
C=int(input("donner votre choix"))
while C>4 :
    print("le produit ne existe pas")
    C=int(input("donner votre choix"))
match C:
    case 1:
        print("combien le produit voulez vous")
        n=int(input())
        while n<0:
            print(" le nombre no valid ")
            n=int(input("veuillez saiser combien le produit voulez vous"))
##CP = contité le produit
        CP=n*400
        print("total HT est :",CP)
        print("total TTC EST:",CP+CP*0.2)
    case 2:
        print("combien le produit voulez vous")
        n=int(input())
        while n<0:
            print(" le nombre no valid ")
            n=int(input("veuillez saiser combien le produit voulez vous"))
##CP = contité le produit
        CP=n*200
        print("total HT est :",CP)
        print("total TTC EST:",CP+CP*0.2)
    
    case 3:
        print("combien le produit voulez vous")
        n=int(input())
        while n<0:
            print(" le nombre no valid ")
            n=int(input("veuillez saiser combien le produit voulez vous"))
##CP = contité le produit
        CP=n*200
        print("total HT est :",CP)
        print("total TTC EST:",CP+CP*0.2)
    case 4:
        print("combien le produit voulez vous")
        n=int(input())
        while n<0:
            print(" le nombre no valid ")
            n=int(input("veuillez saiser combien le produit voulez vous"))
##CP = contité le produit
        CP=n*900
        print("total HT est :",CP)
        print("total TTC EST:",CP+CP*0.2)
    case _:
        print("le aparaille ne existe pas")
