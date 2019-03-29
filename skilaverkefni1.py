# Ragnar Helgi Breiðfjörð Unnþórsson

import random

konni = True
while konni:

    print("1 - listi fyrir tölur")
    print("2 - Random-tölur")
    print("3 - Strengjalisti")
    print("4 - Fjöldi teningakasta ákveðinn af notanda")
    print("5 - Skráning í áfanga")
    print("6 - Hætta")
    val = input("Veldu annaðhvort 1, 2, 3, 4, 5 eða 6 til að hætta: ")

    if val == "1":
        talnalisti = []
        counter = 1
        counter50 = 0

        #ÉG NENNI EKKI AÐ COMMMENTA GRRRRRRRRRRR!
        #Þessi kóði spyr um tölur
        for x in range(7):
            x = int(input("Sláðu inn tölu " + str(counter) + ": "))
            talnalisti.append(x)

            counter = counter + 1

        talnalisti.sort()

        #Þetta prentar út allt dæmið sem það segist gera...
        print("Stærsta talan er", max(talnalisti))
        print("Minnsta talan er", min(talnalisti))
        print("Meðaltalið er", talnalisti[int(len(talnalisti) / 2)])
        print("Summa talnana er", sum(talnalisti))

        #Þetta prentar út talnalistann með smá tricki sem prentar allt út kúl B)
        for x in talnalisti[:-1]:
            print(x, end=";")
        print(talnalisti[6])

        #Þetta finnur allar tölurnar undir eða jafnar 50,5
        for x in talnalisti:
            if x <= 50.5:
                print(x, end=" ")
                counter50 = counter50 + 1
        print()

        print("Það eru", counter50, "tölur undir 50,5. ")

        input("...")

    elif val == "2":
        listi = []
        counter = 0
        counter2 = 0
        counter250 = 0
        counter500 = 0

        #Setur 70 random tölur á bilinu á milli 1 og 500
        for x in range(70):
            x = random.randint(1, 500)
            listi.append(x)

        #Prentar út tölurnar með end= þangað til að counter verður 4 þá prentar það tómt print til að það eru 4 númer í línu
        for x in listi:
            print(x, end="\t")
            counter = counter + 1

            if counter == 4:
                print()
                counter = 0
        print()

        print()
        print("Stærsta talan í listanum er", max(listi))
        print("Minnsta talan í listanum er", min(listi))
        print()

        #Prentar út tölurnar með end= þangað til að counter verður 6 þá prentar það tómt print til að það eru 6 númer í línu
        for x in listi[::-1]:
            print(x, end="\t")
            counter2 = counter2 + 1

            if counter2 == 6:
                print()
                counter2 = 0
        print()

        #Skoðar hversu margar tölur eru í lista á bilinu 1 - 250
        for x in listi:
            if x >= 1:
                if x <= 250:
                    counter250 = counter250 + 1

        #Skoðar hversu margar tölur eru í lista á bilinu 251 - 500
        for x in listi:
            if x >= 251:
                if x <= 500:
                    counter500 = counter500 + 1

        #Prentar fyrverandi niðurstöður út
        print()
        print("Það eru", counter250, "tölur á bilinu 1 - 250")
        print("Það eru", counter500, "tölur á bilinu 251 - 500")
        print()

        input("...")

    elif val == "3":
        listi = []
        counter = 1

        #Setur nöfn í lista
        for x in range(5):
            x = input("Nafn " + str(counter) + ": ")
            listi.append(x)
            counter = counter + 1

        konni123 = True
        while konni123:

            print("1 - Birta nöfnin óraðað")
            print("2 - Raða nöfnunum í stafrófsröð og birta.")
            print("3 - Raða nöfnunum í öfuga stafrófsröð og birta.")
            print("4 - Birta eitt nafn eftir því hvaða númer 1-5 var valið.")
            print("5 - Hætta.")
            eskeetit = input("1, 2, 3, 4 eða 5 til að hætta: ")

            if eskeetit == "1":
                #Prentar út listann óraðaðann
                print(listi)

            elif eskeetit == "2":
                #Prentar út listann raðaðan
                print(sorted(listi))

            elif eskeetit == "3":
                #Prentar út listann raðaðan öfugann
                print(sorted(listi, reverse=True))

            elif eskeetit == "4":
                #Spyr notandann númer hvaða nafn hann vill prenta
                number = int(input("Númer(1, 2, 3, 4 eða 5) hvaða nafn viltu prenta: "))
                print(listi[number - 1])

            elif eskeetit == "5":
                #Endar liðinn
                konni123 = False

            else:
                print("Rangur innsláttur")


    elif val == "4":
        kast = int(input("Hversu oft viltu kasta tening: "))
        listi = []
        countnumbers = {}

        #Setur random tölur í lista með forlykkju sem keyrist eins oft og notandinn segir í kast
        for x in range(kast):
            x = random.randint(1, 6)
            listi.append(x)
            print(x, end=" ")
        print()

        #Telur hversu oft hver einasta tala gerist í listanum
        for num in listi:
            if num in countnumbers:
                countnumbers[num] += 1
            else:
                countnumbers[num] = 1
        print(countnumbers)

        #############

    elif val == "5":
        magnnem = int(input("Hvað eru margir nemendur í FOR1TÖ05BU: "))
        counter = 1
        listi = []

        #Tekur inn hversu oft það á að spurja um nafn og spyr um það mörg nöfn
        for x in range(magnnem):
            x = input("Nafn nemanda " +str(counter)+ ": ")
            listi.append(x)
            counter = counter + 1

        #Sortar listann
        listi.sort()

        #Prentar út listann í starwarsröð
        for x in (listi[:-1]):
            print(x, end=", ")
        print(listi[-1])

    elif val == "6":
        #Slekkur á forritinu...
        print("~Slekkur~")
        konni = False

    else:
        input("Rangur innsláttur, ENTER til að reyna aftur. ")