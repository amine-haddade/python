while True:
 def test_annés(annés):
     if annés%4==0 and annés%100!=0:
         print(" annés est  bissextielles ")
     else:print(" annés non pas bissextielles ")
 a=int(input("donner le annés "))
 test_annés(a)
