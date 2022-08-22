#Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
# Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.
#syötteet
luku_1 = int(input("anna 1. kokonaisluku: "))
luku_2 = int(input("anna 2. kokonaisluku: "))
luku_3 = int(input("anna 3. kokonaisluku: "))

#laskutoimitukset
summa = luku_1 + luku_2 + luku_3
tulo = luku_1 * luku_2 * luku_3
Ka = summa / 3

#tulostukset
print(summa)
print(tulo)
print(Ka)
print(f"ka = {Ka: .2f}")