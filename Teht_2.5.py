#tämän kanssa tarvitsi apua
#syötteet
import math
leiviskä_1 = float(input("Anna leiviskät: "))

naula_1 = float(input("Anna naulat: "))

luoti_1 = float(input("Anna luodit: "))

#laskutoimitukset

naula_2 = (leiviskä_1*20) + naula_1
#leiviskät > nauloiksi
luoti_2 = (naula_2*32) + luoti_1
# naulat > luodeiksi
gramma_1 = (luoti_2*13.3)
# luodit > grammoiksi
gramma_2 = gramma_1 % 1000
# % käytetään unohtamaan vastauksen kokonaisluvut

kilogramma = math.floor(gramma_1/1000)
#math.floor pyöristää alempaan tasalukuun, tällöin ohjelma ei anna vastaukseksi 30kg jne....
print("Annettut massayksiköt nykymuodossa:")
print(f"{kilogramma:.0f} kilogrammaa ja {gramma_2:0.2f} grammaa ")
#                   .0f formatoinnilla ei tule desimaaleja











