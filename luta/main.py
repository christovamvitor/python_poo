from lutadores import *

popo = Boxeador("Popó")
bambam = Boxeador("Bambam")

charles = MMA("Charles do Bronx")
khabib = MMA("Khabib")

print(popo)
print(bambam)
popo.cruzado(bambam)
print(bambam)
popo.gancho(bambam)
print(bambam)
bambam.soco(popo)
print(popo)

print(charles)
print(khabib)
charles.superman_punch(khabib)
print(khabib)