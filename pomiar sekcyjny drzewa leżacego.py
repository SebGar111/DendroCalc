from math import pi
import pandas as pd
high=float(input("podaj wysokość[m]"))


lenght_of_sec=float(input("dlugosc sekcji[m]"))


true_leght_of_sec=high%lenght_of_sec

print(true_leght_of_sec)

leght_of_arrow_without_arrowhead=high-true_leght_of_sec
print(leght_of_arrow_without_arrowhead)
numer_of_complite_sec=leght_of_arrow_without_arrowhead/lenght_of_sec

print(numer_of_complite_sec)

mid_of_sec=lenght_of_sec/2
mid_of_sec=int(mid_of_sec)
summaryvolume=0
b=0+mid_of_sec
#sekcje drzewa
cyfra=0
while  b  <leght_of_arrow_without_arrowhead:
        print(f"Proszę pomierzyć średnice na wysokości {b} m")
        x=float(input('Proszę podać średnicę[cm]'))
        x = (x ** 2 * pi) / 40000 * lenght_of_sec
        x=round(x,3)
        cyfra += 1
        summaryvolume += x
        pomiar=open("Wyniki pomiaru sekcyjnego.py","a+")
        x=str(x)
        pomiar.write(f"miąszość_sekcji_{cyfra}_to_{x}_m3\n")
        pomiar.close()
        print(f"miąszość sekcji {cyfra} wynosi {x}m3")
        print(f"suma miaszosci skecji{round(summaryvolume,3)}")

        b+=lenght_of_sec





#ostatnia sekcja
srednicaniepelnejsekcji=int(input(f"Proszę zmierzyć średnice na wysokości {leght_of_arrow_without_arrowhead}"))

voflastsec=int((srednicaniepelnejsekcji**2*pi/40000)*true_leght_of_sec/3)
print(voflastsec)

volumeofarrow=voflastsec+summaryvolume
print(f"{volumeofarrow} m3-iaszosc drzewa")

