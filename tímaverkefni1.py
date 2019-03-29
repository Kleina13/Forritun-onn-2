# Ragnar Helgi Breiðfjörð Unnþórsson

#Liður 1


#Liður 2
def fjoldiOrda(string):
    return string.count(' ')

def fjoldiB(string):
    return string.count('B') + string.count('b')

def snuaVid(string):
    return string[::-1]

#Liður 3
def flatarmal(lengd, breidd):
    return lengd * breidd

while True:
    print("1 - Listi")
    print("2 - Strengur")
    print("3 - Föll")
    print("4 - Hætta")
    konni = int(input("> "))

    if konni == 1:
        pass

    elif konni == 2:
        strengur = input("Strengur: ")
        print("Það eru", fjoldiOrda(strengur), "orð í textanum.")
        print("Það eru", fjoldiB(strengur), "B/b í textanum.")
        print("það eru", 'óklárað', "tölustafir í textanum")
        print('Strengurinn snúinn við er "' +str(snuaVid(strengur))+ '".')

    elif konni == 3:
        counter = 1
        listi = []
        for x in range(4):
            print("Herbergi", counter)
            b = input("Breidd: ")
            l = input("Lengd: ")
            print()
            f = flatarmal(l, b)
            listi.append(f)
            counter += 1
        print(listi)

    elif konni == 4:
        break

    else:
        print("Rangur innsláttur")