# Ragnar Helgi Breiðfjörð Unnþórsson

konni = True
while konni:
    print("1. Dæmi")
    print("2. Dæmi")
    print("3. Dæmi")
    print("4. Dæmi")
    print("5. Dæmi")
    print("6. Dæmi")
    print("7. Hætta")
    val = input("Veldu annaðhvort 1, 2, 3, 4, 5, 6 eða 7 til að hætta: ")

    if val == "1":
        tal1 = int(input("Sláðu inn tölu 1: "))
        tal2 = int(input("Sláðu inn tölu 2: "))

        plus = tal1 + tal2
        marg = tal1 * tal2

        print("Summa", tal1, "og", tal2, "er", plus)
        print("Margfalda", tal1, "og", tal2, "er", marg)

        input("...")

    elif val == "2":
        first = input("Sláðu inn fornafnið þitt: ")
        second = input("Sláðu inn eftirnafnið þitt: ")

        print("Halló", first, second)

        input("...")

    elif val == "3":
        pass

    elif val == "4":
        pass

    elif val == "5":
        pass

    elif val == "6":
        pass

    elif val == "7":
        print("~Slekkur~")
        konni = False

    else:
        input("Rangur innsláttur, reyndu aftur.")