# Ragnar Helgi Breiðfjörð Unnþórsson

konni = True
while konni:
    print("1. Dæmi")
    print("2. Dæmi")
    print("3. Dæmi")
    print("4. Dæmi")
    print("5. Dæmi")
    print("6. Hætta")
    val = input("Veldu annaðhvort 1, 2, 3, 4, 5, 6 eða 7 til að hætta: ")

    if val == "1":
        print(" ")

        print("~Manneskja 1~")
        nafn1 = input("Nafn: ")
        haed1 = int(input("Hæð CM: "))
        print(" ")

        print("~Manneskja 2~")
        nafn2 = input("Nafn: ")
        haed2 = int(input("Hæð CM: "))
        print(" ")

        if haed1 > haed2:
            print(nafn1, "er hærri en", nafn2)

        elif haed2 > haed1:
            print(nafn2, "er stærri en", nafn1)

        elif haed1 == haed2:
            print(nafn1, "og", nafn2, "eru jafnhá")

        input(" ")

    elif val == "2":
        print(" ")

        lm = int(input("Lengd í metrum: "))
        bm = int(input("Breidd í metrum: "))

        lb = lm * bm
        ekrur = lb / 4046

        print("Þessi reitur er", ekrur, "ekrur")

        input(" ")

    elif val == "3":
        print(" ")

        lengd = 10

        breidd = int(input("Breidd Fernings í metrum: "))

        print("Stærð \t Lengd í ekrum")

        while lengd != 210:
            k = lengd * breidd
            ekrar = k / 4046
            print(lengd, "\t", ekrar)
            lengd = lengd + 10

        input(" ")

    elif val == "4":
        print(" ")

        afangilist = []
        bokstafur = False
        tolustafur = False

        afangi = input("Skammstöfun áfanga: ")

        for x in afangi:
            afangilist.append(x)

        for x in afangilist[1, 4]:
            if x.isupper:
                bokstafur = True

        for x in afangilist[4, 8]:
            if x.isdigit:
                tolustafur = True

        if bokstafur == False:
            print(afangilist[1, 4], "eru ekki allir hástafir. ")

        elif tolustafur == False:
            print(afangilist[4, 8], "eru ekki allir tölustafir. ")

        else:
            print("Þetta er rétt skammstöfun áfanga. ")


    elif val == "5":
        pass

    elif val == "6":
        print("~Slekkur~")
        konni = False

    else:
        input("Rangur innsláttur, Reyndu aftur")