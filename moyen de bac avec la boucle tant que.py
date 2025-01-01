n=int(input("donner le nombre de étudient"))
for i in range(0,n):
    print("donner le nom du étudient")
    nom=input()
    N=float(input("donner la not de national"))
    while N>20 or N<0 :
        print("not invalid")
        N=float(input("donner la not de national"))
    R=float(input("donner la not de régional"))
    while R>20 or R<0 :
        print("not invalid")
        R=float(input("donner la not de régionale"))
    C=float(input(" donner la note de control contunue"))
    while C>20 or C<0 :
        print("not invalid")
        C=float(input("donner la not de control contunue"))
    M=N*0.5+R*0.25+C*0.25
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
