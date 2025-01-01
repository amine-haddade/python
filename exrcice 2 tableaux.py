def lir (T,n):
    for i in range(n):
        print("donner le nombre",i+1)
        g=int(input())
        T.append(g)
def afficher(T,n):
    for i in range(n):
        print(T[i])


                    #exrcice 2
tableaux1=[]        
lir(tableaux1,int(input("donner indice de tablaeux  1  ")))


                    #afficher(tableaux1,len(tableaux1))
print(tableaux1)
tableaux2=[]        
lir(tableaux2,int(input("donner indice de tablaeux  2  ")))


                     #afficher(tableaux2,len(tableaux2))
print(tableaux2)
tableaux3=[]
for i in range (len(tableaux2)):
    tableaux3.append(tableaux1[i]+tableaux2[i])
print(3*"\n",tableaux3)



                     #exercice 3:::::::
T1=[]
aa=int(input("donner le dimonsio  de tableaux 1\n"))
lir(T1,(aa))
print(T1)

T2=[]
bb=int(input("donner le dimonsio  de tableaux 2\n"))
lir(T2,bb)
print(T2)
T3=[]
for i in range(aa):
       T3.append(T1[i])
for j in range(aa,bb+aa):
       T3.append(T2[j-aa])
print(T3)
       
       

       
       

        
