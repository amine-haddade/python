n=int(input("donner le nombre de étudient\n"))
for i in range(0,n):
    print(" donner le nom du étudient\n")
    nom=input()
    N=float(input("donner la not de national\n"))
    R=float(input("donner la not de régionale\n"))
    c=float(input(" donner la note de control contunue\n"))
    M=N*0.5+R*0.25+c*0.25
    print(" le moyene de ",nom,"est",M,)
    if M<10 and M>=7:
         print(" ratt ")
    elif M>=10 and M<12:
         print("bass")
    elif M>=12 and M<14:
         print (" a.bien ")

    elif M>=14 and M<16:
         print ("bien")

    elif M>=16 and M<18:
         print (" trés bien ")

    elif M>=18 and M<20:
         print("éxelant")
    elif M==20:
         print(" wowowowowo ")
    elif M<7 :
         print("nom valide")
    else:
         print ("not invalid ")
     


    
    
            
    
    
