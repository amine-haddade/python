import random
ch=["orange","kiwi","fraise","pomme"]
e=random.choice(ch)
print(e)
# e c'est le mot qui choisire 
t=[e]
# t c'est le tableau qui contien le mot qui choisir pa  def random
#print(t)
r=[]
#r c'est le tableau remplir dans chian de caractere
for i in e:
    r.append(i)
print(len(r))
def remp(o):
    for i in range(len(r)):
        o.append("*")
    return(o)
o=[]
print(remp(o))
#  principale  #
cp=0
po=0


while True:
    print("donner une caractere")
    c=(input())
    if(c>="a" or c<="z") and (c in r):
      if c in o:
          tt=r.index(c)
          #tt c'se le indice de cractére c
          
          for ii in range (tt+1,len(o)):
              if c in o:
                  oo=r.index(c)
                  o[oo]=c
                  print(o)
                  break
      else:
       i=r.index(c)
       o[i]=c
       po=po+1
       print(o)
       if  len(o)==po: 
           print(" bravo tu as terminer le tableau")
           break

    else:
       cp=cp+1
       if cp==5:
          print("désoler vous avez terminer touts vos tentatives")(c)
          break




    


    

    










 



    
    


          



