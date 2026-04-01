vendeg = int(input("Hány vendég van?"))
raktar = int(input("Mennyi tojás van raktáron?"))

szukseg_tojas = round(vendeg * 3)
szukseg = round(szukseg_tojas * 1.1)

meg_kell = round(szukseg - raktar)

if raktar >= szukseg :
    print(f"{raktar} db tojás elegendő {vendeg} vendég számára.")
else :
    print(f"Még {meg_kell} db tojásra lesz szükség!")

print(f"Vendégek száma: {vendeg}")
print(f"Raktáron lévő tojások száma: {raktar}")