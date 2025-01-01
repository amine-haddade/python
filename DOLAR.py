while True:
 Ms=int(input("  BONJOUR 🎃🎃🎃☺☺☺☺DONNER LE MONTANT🎃🎃🎃  "))
 if (Ms>100):
       P=Ms//100
       print("Nombre de billets de 100 est",P)
       D=(Ms%100)//20
       print("Nombre de billets de 20 est",D)
       E=((Ms%100)%20)//10
       print("le Nombre de billets de 10 est",E)
       H=(((Ms%100)%20)%10)//5       
       if H>0:
              print("le nombre de billets de 5 est",H)
 elif Ms<100 and Ms>20:
        J=Ms//20
        print("le nombre de billets de 20 est",J)
        K=Ms%20//10
        print("lenombre de billets de 10 est",K)
        G=((Ms%20)%10)//5
        if(G>0):
                print("lenombre de billets de 5 est",G)
 
 elif Ms<20 and Ms>10:
        L=Ms//10
        print("le nombre de billiets de 10 est",L)
        Z=(Ms%10)//5
        if Z>0:
             print(" le nobre de billets de 5 est ",Z)
 elif Ms<10 and Ms>0:
     A=Ms//5
     print(" le nombre de billets de 5 est ",A)
 else:
        print("le montant invalid")
