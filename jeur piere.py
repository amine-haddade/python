while True:
 import random
 BOXchj_o=0
 BOXchj2=0
 print("1 piere ; 2 siseaux ; 3 papie")
 chj_o=random.randint(1,3)
 chj2=int(input("donner votre choix\n"))
 print("moi je vais choisir\n",chj_o)
 while chj2>3 or chj2<1:
    print("le choix n’éxcicte pas donner choi")
    chj2=int(input())
    chj_o=random.randint(1,3)
    print("moi je vais choisir\n",chj_o)
 if chj_o==chj2:
     print("match null")
 elif chj_o==1 and chj2==2:
     print(" moi ganger 3")
     BOXchj_o+=1
 elif chj_o==1 and chj2==3:
     print(" tu as gagné ")
     BOXchj2+=1
 elif chj_o==2 and chj2==1:
     print("tu as gagné")
     BOXchj2+=1
     
 elif chj_o==2 and chj2==3:
     print("tu as gagné")
     BOXchj2+=1
 elif chj_o==3 and chj2==1:
     print(" moi gagné")
     BOXchj_o+=1
 else:
     chj_o==3 and chj2==2
     print("moi gagné")
     BOXchj_o+=1
 if BOXchj2 == 3:
        print("Tu as gagné le match !")
        break
 elif BOXchj_o == 3:
        print("Moi, j'ai gagné le match !")
        break
