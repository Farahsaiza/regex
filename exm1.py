import re

exemple='''
        P1 est un produit compose de P2 et P3 

        P2 est un produit elementaire 

        P5 est un produit compose de P1 et P4

        P4 est un produit elementaire 

        P9 est un produit compose de P1,P6 et P4

        P10 est un produit compose de P3 et P5

        P11 est un produit compose de P5 et P3 '''


e=re.findall(r'P\d+ est un produit elementaire',exemple)
print("les produits elementaire sont :",e)

c=re.findall(r'P\d+ est un produit compose de P\d,P\d et P\d',exemple)
print("les produits compose sont :" ,c)

K=re.findall(r'P\d+ est un produit compose de P3 et P5|P\d+ est un produit compose de P5 et P3',exemple)
print("les produits conpse de P3 et P5 sont :" ,K)

b=re.findall(r'P\d+ est un produit compose de P1 et P4|P\d+ est un produit compose de P1,P6 et P4|P\d+ est un produit compose de P3 et P5|P\d+ est un produit compose de P5 et P3',exemple)
print("les produits compose qui n'ont pas P2 dans leurs compositions sont: ",b) 

a=re.findall(r'P\d + est un produit compose de P9',exemple)
if a!=[]:
    print("les produit composes de P9 sont :",a)
else:
    print("les produit composes de P9 n'existe pas ")





 
