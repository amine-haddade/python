def montant_pientur(nbr_t,p_kg,nbr_kg):
    MP=nbr_t*p_kg*nbr_kg
    print("le charge de piendre",MP)
print("donner le nombre de tage ")
nbr_t=int(input())
p_kg=float(input(" saiser le prix  de kg de pienture \n "))
nbr_kg=int(input("donner le nomnre de kulo le piendre \n"))
montant_pientur(nbr_t,p_kg,nbr_kg)
def montant_employer(n_e,p_j,n_j):
    ME=n_e*p_j*n_j
    print("le montant des employé est ",ME)
n_e=int(input(" deonner le nombre de employé travaile dans le project\n"))
p_j=float(input(" saiser le prix de une employé dans seul jour\n "))
n_j=int(input(" donner le nombre de joure travailler \n "))
montant_employer(n_e,p_j,n_j)

