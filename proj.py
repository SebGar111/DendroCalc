from random import randint
from pynput.keyboard import Key, Listener
import re

def game():
    game_width = 15
    game_high = 15
    key_x=3#randint(0,game_width)
    key_y=4#randint(0,game_high)

    x=0
    y=0

    if key_x ==3 and key_y ==3:
        game()
    if key_x == 7 and key_y == 4:
        game()
    if key_x == 9 and key_y == 9:
        game()

    steps = 0
    Did_player_found_the_torch=False
    print(f"{name + odmiana}!Zaczynamy rozgrywke!")
    while not Did_player_found_the_torch:
        steps+=1
        print()


        move = input(f"Gdzie jest butelka,{name+odmiana}?")

        match move.lower():
            case  "w":
                  y += 1
                  if y > game_high:
                   print('siatka ogrodzenia')
                   y = game_high
            case  "s",:
                y -= 1
                if y < 0:
                    print('siatka ogrodzenia')
                    y = game_high
            case   'a':
                x += 1
                if x > game_width:
                    print('siatka ogrodzenia')
                    x = game_width
            case    'd':
                x-=1
                if x < 0:
                 print('siatka ogrodzenia')
                 x = game_width
            case     "q":
                print('koniec')
                quit()

            case '':
             print('Niewłaściwy klawisz!')
             continue


        if x == key_x and y == key_y:
            print("Latarka znaleziona")
            print("Gratulacje")
            zapytanie_o_kontynuacje()

        if x == 3 and y == 3:
            print("rów, wracasz na początek")
            y = 0
            x = 0
        if x == 7 and y == 4:
            print("rów, wracasz na początek")
            y = 0
            x = 0
        if x == 9 and y == 9:
            print("rów, wracasz na początek")
            y = 0
            x = 0

        distance1 = abs(x - key_x) + abs(y - key_y)
        if distance1 >= 5:
            print("Ciemno")

        elif distance1 < 5 or distance1 >2:
            print("Szaro")
        elif distance1 == 2:
            print('Ciepło')
        elif distance1 <=1:
            print("gorąco")


        print(f"wektor wschód/zachód {x} wektor północ/południe {y}")
        print(steps)

#gra cieplo zimno (szukanie latatrki na skawistym biwaku z mozliwoscia wpadniecia do rowu)
#jesli gracz pojawi sie na polach (3,3),(7,4),(9,9) cofa sie na poczatek
name = input(str('Podaj swoje imie'))

odmiana = ''

if name[-1] == "n" or name[-1]=='w' or name[-1]=='f':
    odmiana = "ie"

elif name[-1] == "b":
    odmiana = "ie"
elif name == "Bartek" or name == "bartek":
    name = 'Bartku'
    odmiana = ""
elif name[-1] == "l" or name[-1] == "ł":
    name = re.sub(r'[ł,l,e]', '', name)
    odmiana = "le"
elif name == "Eugeniusz" or name =='eugeniusz':
    name = "Eugeniuszu"
    odmiana = ''
elif name[-1] == "r":
    odmiana = "ze"

elif name[-1] == 'a' and not name.capitalize() == 'Kuba':
    
    print('Dowidzenia!!!')
    quit()

elif name == 'Kuba' or name == 'kuba':
    name = 'Kubo'
    odmiana = ''
else:

     name = re.sub(r'[e]', '', name)
     odmiana ='u'
#funkcja pytająca się gracza czy chce kontynuować
def zapytanie_o_kontynuacje():
    print('Czy chcesz grac dalej? tak/nie')
    #try:

    q2 = (input("Wybór"))
    q2=q2.lower()
    #except TypeError:
    print("Tylko wyrazy tak/nie!")



    if q2 == 'tak':
        print("Witamy ponownie")
        game()
    elif q2  == 'nie':
        quit()
    else:
        zapytanie_o_kontynuacje()







game()

