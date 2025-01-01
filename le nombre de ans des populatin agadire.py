nbr_ans=int
p_marak=1000000
p_agadi=500000
nbr_ans=0
while (p_marak>p_agadi):
    p_marak=p_marak+50000
    p_agadi=p_agadi+p_agadi*0.08
    nbr_ans=nbr_ans+1
    print(nbr_ans)
print(" le nombre de anés qui agadir dépassera marakech DANS la population C'est un",nbr_ans,"ans")
