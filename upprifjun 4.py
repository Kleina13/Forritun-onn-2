# Ragnar Helgi Breiðfjörð Unnþórsson

import random

konni = True
while konni:
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. ")
    print("5. ")
    print("6. Hætta")
    val = input("1,2,3,4,5 eða 6 til að hætta: ")

    if val == "1":
        Nn = 0
        setning = input("Skrifaðu setningu: ").lower()

        for x in setning:
            if x == "n":
                Nn = Nn + 1

        print("Það eru", Nn, "í setninguni.")

        input("...")

    elif val == "2":
        nafn1 = input("Sláðu inn fyrsta nafnið: ")
        nafn2 = input("Sláðu inn seinna nafnið: ")

        if len(nafn1) == len(nafn2):
            for x in range(len(nafn1)):
                if nafn1[x] == nafn2[x]:
                    print("Stafur nr", x + 1, "er sami og í", nafn1[x])

        input("...")

    elif val == "3":
        nafn = input("Sláðu inn nafn: ").lower()
        Rnafn = nafn[::-1]

        if nafn == Rnafn:
            print("Nafnið", nafn[0].upper()+nafn[1:30], "er samhverft")

        else:
            print("Nafnið", nafn[0].upper()+nafn[1:30], "er ekki samhverft")

        input("...")

    elif val == "4":
        setning = input("Sláðu inn setningu: ")
        ja = True
        while ja:
            print("1. Fjöldi orða")
            print("2. Finna orð")
            print("3. Lengd strengs")
            print("4. Öfugur strengur")
            print("5. Tölur í lista")
            print("6. Leita af stórum staf ")
            print("7. Breyta í A")
            print("0. Hætta")
            valmynd = input("Veldu: ")

            if valmynd == "1":
                tel = 1

                for x in setning:
                    if x == " ":
                        tel = tel + 1

                print(tel)

                input("...")

            elif valmynd == "2":
                ordhluti = input("Finna orð: ")

                if ordhluti in setning:
                    print("Fann")

                else:
                    print("Ekki til")

                input("...")

            elif valmynd == "3":
                print("lengd strengs er", len(setning))

                input("...")

            elif valmynd == "4":
                print("Öfugt er það", setning[::-1])

                input("...")

            elif valmynd == "5":
                print(setning.upper())

                input("...")

            elif valmynd == "6":
                pass

            elif valmynd == "7":
                print(setning.replace("a", "A"))

                input("...")

            elif valmynd == "0":
                ja = False

    elif val == "5":
        listi = []
        n267 = 0
        low = 1000
        lowtel = 0
        B = 0

        for x in range(100):
            tala = random.randint(250, 401)
            listi.append(tala)
        summa = sum(listi)/len(listi)
        print("Meðal talið þitt", summa)

        for x in listi:
            if x <= 267:
                n267 = n267 + 1

        print("Það eru ", n267, "tölur undir 267")

        for x in listi:
            if x < low:
                low = x

        for x in listi:
            if x == low:
                lowtel = lowtel + 1

        print("Lægsta talan er", low, "og hún kom upp", lowtel, "sinnum")

        for x in listi:
            if x >= 300:
                if x <= 350:
                    B = B + 1
        print(B)

        for x in listi:
            print(x, end=" ")
        print("\n")

        input("...")

    elif val == "6":
        print("~Slekkur~")
        konni = False

    else:
        input("Rangur innsláttur")