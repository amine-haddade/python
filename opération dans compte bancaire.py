while True:
 print("veuillez saiser le montant ")
 M=int(input())
 if (M>0):
     print("pour retrait taper ;R; pour dépot tapez ;D;")
     C=input("donner votre choix")
     match C:
         case "R":
             print("donner le montan que vou souhaitez retrai")
             S=int(input())
##S=le montant retrait
             if (S<=M and S>0):
                 print("le montan restant est",M-S)
             elif S>M and S>0 :
                     print(" désoler le montan que vois retrais ne existe pas ")
             else :
                     print("opératin no valide")
                    
         case "D":
             print(" donnez le montan dépot")
             Z=int(input())
##Z=le montant DEPOT
             if Z>0:
                print(" le montan actuel est",M+Z)
             if Z<=0:
                 print("le montant que vous déposetr no valide ")
         case _:
             print(" le choix ne existe pas ")
 if M<=0:
     print(" le montant no valide")
