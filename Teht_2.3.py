#Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

kanta = float (input("Anna suorakulmion kanta: "))
korkeus = float (input("Anna suorakulmion korkeus: "))

#laskutoimitukset
A = kanta * korkeus
piiri = (kanta * 2) + (korkeus * 2)

#tulostukset
print(f"Ala = {A}")
print(f"piiri = {piiri}")

