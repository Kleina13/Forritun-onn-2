#Ragnar Helgi Breiðfjörð Unnþórsson

import math

def kula(rd):
    outcome = (4 * math.pi * pow(rd, 3)) / 3
    return outcome

def kassa(l, b, h):
    outcome = (l * b * h)
    return outcome

def triangle(b, h):
    outcome = (b * h) / 2
    return outcome

konni = True
while konni:

    print("1 - Rúmmál kúlu")
    print("2 - Rúmmál kassa")
    print("3 - Flatarmál þrýhirnings")
    print("4 - Hætta")

    choice = input(" : ")

    if choice == "1":
        radius = int(input("Sláðu inn radius kúlunnar"))
        rummal = kula(radius)
        print("Rúmmál kúlurnar er:", round(rummal, 2))

    elif choice == "2":
        l = int(input("Lengd: "))
        b = int(input("Breidd: "))
        h = int(input("Hæð: "))
        rummal = kassa(l, b, h)
        print("Rúmmál kassans er:", round(rummal, 3))

    elif choice == "3":
        b = int(input("Breidd: "))
        h = int(input("Hæð: "))
        flatarmal = triangle(b, h)
        print("Flatarmál þrýhirnings er:", round(flatarmal))

    elif choice == "4":
        konni = False