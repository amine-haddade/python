"""def partir(t,n):
    for i in range(n):
        print(" donner élement",i+1)
        n=int(input())
        t.append(n)

      
t=[]
print(" donner la dimonsion")
d=int(input())
partir(t,d)
n=[]
for i in t:
    n.append(i*2)
print(t)
print(n)"""

#les diction yotube français
"""eleves={"poul":{"not":15,"apreciation":"c'est un bonne note rien a dire"
                },
        "amine":{"not":17,"apreciation":"rien a dire eleve au tope"
                 }}
eleves["moha"]={"not":12,"apreciation":"attention moha tu ne peut jamais travaille"}
eleves["poul"]["not"]=20
for eleve in eleves:
    print(eleves[eleve]["not"],":",eleves[eleve]["apreciation"])
if "amine" in eleves.keys():
    print("vrai")"""
joueurs={"cr7":{"equib":"naser","position":7}
         ,"messi":{"equib":"maimi","position":10}
         ,"naymar":{"equib":"hilal","position":10},}
joueurs["amine"]={"equib":"raja","position":8
                  }
joueurs["amine"]["equib"]="reial"
del joueurs["amine"]
#o=joueurs.get("cr7")
#print(o)
for i in joueurs:
    print(joueurs[i]["equib"],joueurs[i]["position"])
if "naymar" in joueurs:
    print(True)



