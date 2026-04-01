from urhajo_class import Urhajos

urhajosok = []

with open('02_Python/urhajos.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        urhajos = Urhajos(adatok[0], adatok[1], adatok[2], int(adatok[3]), int(adatok[4]))
        urhajosok.append(urhajos)

# for urhajos in urhajosok:
#     print(urhajos.nev, urhajos.orszag, urhajos.nem, urhajos.szulev, urhajos.urido)

mennyi = len(urhajosok)
print(f"3.4. feladat: Az állományban {mennyi} űrhajós adatai találhatók.")

olaszok = False

for urhajos in urhajosok:
    if urhajos.orszag == 'ITA':
        olaszok = True
        break

if(olaszok):
    print(f'3.5. feladat: Az űrhajósok között van olasz származású.')
else:
    print(f'3.5. feladat: Az űrhajósok között nincs olasz származású.')

nok = []

for urhajos in urhajosok:
    if urhajos.nem == 'N':
        nok.append(urhajos.urido)

print(nok)

atlag = sum(nok) / len(nok)

print(f'3.6. feladat: A női űrhajósok átlagosan {atlag:.2f} napot töltöttek az űrben.')

evszam = []

for urhajos in urhajosok:
    evszam.append(urhajos.szulev)

legfiatalabb = max(evszam)

for urhajos in urhajosok:
    if urhajos.szulev == legfiatalabb:
        break
print(f'3.7. feladat: A legfiatalabb űrhajós: Neve: {urhajos.nev} Országa: {urhajos.orszag} Neme: {urhajos.nem} Születési éve: {urhajos.szulev} Űrben töltött ideje: {urhajos.urido} nap.')