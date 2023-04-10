#d1,3 = średnica rzewa na wysokość 1,3m(pierśnica)
#d= średnica rzewa na danej wysokosci
#g=pole przekroju strzały
#h = wysokosc
from math import pi
#(d^2*pi)/40000
class CalcVmiaszosci:
    def __init__(self,grubosc_1trzecia,grubosc_maxH,grubosc,wysokosc,grubosc_srodek,grubosc_podstawa,poleprzekroju):
        self.grubosc_1trzecia=grubosc_1trzecia
        self.grubosc_maxH = grubosc_maxH
        self.grubosc=grubosc
        self.wysokosc=wysokosc
        self.grubosc_srodek=grubosc_srodek
        self.grubosc_podstawa=grubosc_podstawa
        self.poleprzekroju=poleprzekroju


    def Hossfeld(self):
         return ((self.grubosc_1trzecia**2*pi/40000+self.grubosc_maxH**2*pi/40000)/4)*self.wysokosc



    def Smalennian(self):
        return (((3*self.grubosc_podstawa**2*pi/40000) +self.grubosc_maxH**2*pi/40000)/2)*self.wysokosc

    def Hubera(self):
        return self.grubosc_srodek**2*pi/40000*self.wysokosc
    def zmienne(self):
        self.grubosc_maxH=float(input("Podaj grubosc maks [w cm]"))
        self.grubosc_podstawa=float(input("Podaj grubosc przy podstawie [w cm]"))
        self.grubosc_srodek=float(input("Podaj grubosc na środku strzały [w cm]"))




wybor=int(input('Jakim wzorem chcesz obliczyc strzale?'))
calc1 = CalcVmiaszosci(0, 0, 0, 0, 0, 0, 0)
def huber():

    calc1.grubosc_srodek=float(input("Grubosc srodek w cm"))
    calc1.wysokosc=float(input("Proszę podać wysokość"))
    print(f'miąszość drzewa wynosi {calc1.Hubera()}m3')
def hossfeld():

     calc1.grubosc_1trzecia=float(input("Grubosc w1/3 długości(l) w cm"))
     calc1.wysokosc=float(input("Proszę podać wysokość"))
     calc1.grubosc_maxH = float(input("Grubosc na końcu strzały(l) w cm"))
     print(f'miąszość drzewa wynosi {calc1.Hossfeld()}m3')
def smallenian():

     calc1.grubosc_podstawa=float(input("Grubosc max w cm"))
     calc1.wysokosc=float(input("Proszę podać wysokość"))
     calc1.grubosc_podstawa= (calc1.grubosc_podstawa**2*pi)/40000
     print(f'miąszość drzewa wynosi {calc1.Smalennian()}               m3')

if wybor == 1:
    huber()
if wybor ==2:
    hossfeld()
if wybor ==3:
    smallenian()






