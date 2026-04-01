import random
MIN = 4
MAX=8

dobasok = [random.randint(1, 12) for x in range(150)]

print(dobasok)

def kozte(szam, min, max):
    if szam >= min and szam <= max:
        return True
    else:
        return False

truek = 0

for i in range(150):
    dobas = random.randint(1, 12)
    valasz = kozte(dobas, MIN, MAX)
    if valasz == True:
        truek += 1

atlag = (truek / 150) *100

print(f'A 150 dobásból {truek} esett 4 és 8 közé. Ez az összes dobás {atlag:.2f}-a.')