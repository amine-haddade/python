print("bonjeur bien venu dans une magasin ")
print("1:     tv\n 2:        smartch watch\n 3:      portaple apele\n 4:      heure \n 5 :     écoute sans filles")
choix=int(input())
while (choix>4 or choix<0):
    print(" le cois néxiste pas ")
    choix=int(input(" donner votre coix"))
match choix :
    case 1:
        print(" nous avons deux type des tv \n pour choisre tv samsange taper 1 \pour choisir dell taper 2 ")
        choi=int(input())
        while choi>2 or choi<0:
            print(" le cois néxiste pas ")
            print(" donner votre coix")
            choi=int(input())
        match choi:
            case 1:
                print(" souhaiter = 2500")
            case 2 :
                print(" souhaiter = 2300")
    case 2 :
        print(" souhaiter = 1000")
    case 3 :
        print(" souhaiter = 6000")
    case 4 :
         print("souhaiter = 500")        
    case 5:
        print(" souhaiter = 100")


