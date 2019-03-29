# Ragnar Helgi Breiðfjörð Unnþórsson

from random import *

#Liður 1
# Breytir Celsius í Farenheit, tekur inn cel og skilar farenheit
def fahrenheit(celsius):
    return celsius * 1.8 + 32

def celsius(fahrenheit):
    return int((float(fahrenheit) - 32) / 1.8) # Breytir Farenheit í Celsius

#Liður 2
def kelvin(celsius):
    return int(celsius) + 273.15 # Breytir Celsius í Kelvin

def celsiusK(kelvin):
    return kelvin - 273.15 # Breytir Kelvin í Celsius

#Liður 3
def veldi(x, veldi):
    margfeldi = 1
    for i in range(veldi):
        margfeldi *= x
    return margfeldi # Finnur grunntöluna í veldi

#Liður 4
def tomma(cm):
    return cm / 2.54 # Breytir CM í Tommu

def cm(tomma):
    return tomma * 2.54 # Breytur Tommu í CM

#Liður 5
def gallon(liter):
    return liter / 3.785 # Breytir Liter í Gallon

def liter(gallon):
    return gallon * 3.785 # Breytir Gallon í Liter

#Liður 6
def heilsa(nafn, kyn):
    if kyn == 'kk':
        return "Sæll og blessaður " + nafn # Svarar Karlkyns
    elif kyn == 'kvk':
        return "Sæl og blessuð " + nafn # Svarar Kvenkyns
    else:
        return "Halló " + nafn + ", ég kannast ekki við kynið þitt" # Þekkir ekki kynið

#Liður 7
def kasta():
    return randint(1, 7) # Gefur random tölu á bilinu 1 - 7

#Liður 8
def samanbera(list1, list2):
    same = []
    if list1 > list2:
        for i in list1:
            if i in list2 and i not in same:
                same.append(i) # tekur inn allar tölur sem eru eins í list1 og list2
    elif list1 < list2:
        for i in list2:
            if i in list1 and i not in same:
                same.append(i) # tekur inn allar tölur sem eru eins í list2 og list1
    return same

#Kúl while loopa
while True:
    print("1 - Celsíus Farenheit")
    print("2 - Celsíus Kelvin")
    print("3 - Veldisreikningur")
    print("4 - Tommur eða cm")
    print("5 - Lítrar eða gallon")
    print("6 - Kveðja")
    print("7 - Teningakast")
    print("8 - Listar")
    print("9 - Hætta")
    konni = input(" : ")

    if konni == "1":
        print("1. [F/C]")
        print("2. [C/F]")
        val = int(input(" : "))

        if val == 1:
            cel = int(input("Celsius: "))
            print(cel, "°C er", fahrenheit(cel), "°F")

        elif val == 2:
            fahren = int(input("Fahrenheit: "))
            print(fahren, "°F er", celsius(fahren), "°C")

    elif konni == "2":
        print("1. [K/C]")
        print("2. [C/K]")
        val = int(input(" : "))

        if val == 1:
            cel = int(input("Celsius: "))
            print(cel, "°C er", kelvin(cel), "K")

        elif val == 2:
            kelv = int(input("Kelvin: "))
            print(kelv, "K er", celsiusK(kelv), "°C")

    elif konni == "3":
        tala = int(input("Sláðu inn tölu: "))
        veldistala = int(input("Sláðu inn veldi"))
        print(tala, "í", veldistala, "veldi er", veldi(tala, veldistala))

    elif konni == "4":
        print("1. [T/Cm]")
        print("2. [Cm/T]")
        val = int(input(" : "))

        if val == 1:
            cm = int(input("Sentimetrar: "))
            print(cm, "Cm eru", tomma(cm), "tommur")

        elif val == 2:
            tom = int(input("Tommur: "))
            print(tom, "tommur eru", cm(tom), "Cm")

    elif konni == "5":
        print("1. [L/Ga]")
        print("2. [Ga/L]")
        val = int(input(" : "))

        if val == 1:
            ga = int(input("Gallons: "))
            print(ga, "gallons eru", liter(ga), "lítrar")

        elif val == 2:
            l = int(input("Lítrar: "))
            print(l, "lítrar eru", gallon(l), "gallons")

    elif konni == "6":
        nafn = input("Nafn: ")
        kyn = input("Kyn[KK/KVK]: ").lower()
        print(heilsa(nafn, kyn))

    elif konni == "7":
        while True:
            print(kasta())
            aftur = input("Viltu kasta aftur [J/N]").lower()
            if aftur == "n":
                break
            print()

    elif konni == "8":
        listiA = []
        listiB = []

        counter = 1
        amountA = int(input("Magn af tölum í lista A: "))
        for l in range(amountA):
            l = int(input("Tala " + str(counter) + ": "))
            listiA.append(l)
            counter += 1

        counter = 1
        amountB = int(input("Magn af tölum í lista B: "))
        for l in range(amountB):
            l = int(input("Tala " + str(counter) + ": "))
            listiB.append(l)
            counter += 1

        print(samanbera(listiA, listiB))

    elif konni == "9":
        print("~Slekkur~")
        break # Endar loopuna