#Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
#MAtematiikkaan tarvitsee matematiikan kirjastoa!
import math

r = (float) (input ("anna ympyrän säde:"))

ala = math.pi * math.pow(r,2)

print(f"ympyrän pinta-ala on: {ala: .3f}")

