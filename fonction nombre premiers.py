def crible_eratosthene(n):
    # Créez une liste de booléens pour représenter les nombres de 2 à n.
    # Initialisez-les tous à True, ce qui signifie qu'au départ, nous supposons que tous les nombres sont premiers.
    est_premier = [True] * (n + 1)
    est_premier[0] = est_premier[1] = False  # 0 et 1 ne sont pas premiers.

    p = 2
    while p * p <= n:
        if est_premier[p]:
            # Si p est premier, marquez tous ses multiples comme non premiers.
            for i in range(p * p, n + 1, p):
                est_premier[i] = False
        p += 1

    # Maintenant, la liste est_premier contient True pour les nombres premiers et False pour les non premiers.
    nombres_premiers = [i for i in range(2, n + 1) if est_premier[i]]
    return nombres_premiers

# Spécifiez l'intervalle de recherche
debut = 1
fin = 100

nombres_premiers = crible_eratosthene(fin)
nombres_premiers = [x for x in nombres_premiers if x >= debut]  # Filtrer les nombres premiers dans l'intervalle

print("Nombres premiers entre", debut, "et", fin, "sont:", nombres_premiers)
