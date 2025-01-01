clien={}
compte={}
cliencompte={}
print("======================gestion bancaire======================")
print("1_agent\n2_client")
print(" donner votre privilage")
ch=int(input())
while ch!=1 and ch!=2:
    print(" donner votre privilage")
    ch=int(input()) 
match ch :
    case 1:
        print("1_pour ajouter un compte\n2_pour supprimer un compte ")
        cha=int(input(" saisir votre choix"))
        match cha :
            case 1:
                #def ajouter un clase 2:
                #def supprimer un compte 
    case 2:
        print("1-pour modifier pass\n2-pour afficher le solde\n3-pour diposer un montant\n4-pour retaire ")
        
                
