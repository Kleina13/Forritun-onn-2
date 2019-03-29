#Ragnar Helgi Breiðfjörð Unnþórsson

#Byrjun lið 1
def skrifaut(list):
    for number in list[:-1]:
        print(number, end=", ")
    print(list[-1])

def stærsta(list):
    big = list[0]
    for number in list:
        if number > big:
            big = number
    print(big)

def minnsta(list):
    small = list[0]
    for number in list:
        if number < small:
            small = number
    print(small)

def summa(list):
    answer = 0
    for number in list:
        answer += number
    print(answer)

def meðaltal(list):
    average = 0
    division = 0
    for number in list:
        average += number
        division += 1
    print(average / division)
#Lok lið 1

#Byrjun lið 2
def setning(name='Ragnar', home='Birkigrund 21', proffesion='Fátækur námsmaður', hobby='Tölvuleikir'):
    print("Nafn:", name, "|", "Heimili:", home, "|", "Atvinna:", proffesion, "|", "Áhugamál:", hobby, "|")
#Lok lið 2


#Byrjun lið 3
def uhm(*tolur):
    division = 0
    for number in tolur:
        division += 1
    print(sum(tolur) / division)
#Lok lið 3

#Byrjun lið 4
def texti(text, word):
    if text.count(word) >= 1:
        return True
#Lok lið 4

kONni = True
while kONni:
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. ")
    print("5. Hætta")
    val = input(" : ")

    if val == '1':
        listi = []

        for x in range(5):
            x = int(input("tala:"))
            listi.append(x)

        print()
        skrifaut(listi)
        stærsta(listi)
        minnsta(listi)
        summa(listi)
        meðaltal(listi)
        print()

    elif val == '2':
        setning()
        setning("Lárus")
        setning("Lárus", "Sólargata 31")
        setning("Lárus", "Sólargata 31", "Veiðimaður")
        setning("Lárus", "Sólargata 31", "Veiðimaður", "Píanó")

    elif val == '3':
        uhm(1, 2, 43, 5)
        uhm(4, 23, 4)
        uhm(126, 43, 231, 3, 2354)

    elif val == '4':
        text = 'Ég elska jarðaber'
        word = 'elska'

        if texti(text, word):
            print("Orðið", '"'+word+'"', "er í textanum.")

        else:
            print("Orðið", '"'+word+'"', "er ekki í textanum.")

    elif val == '5':
        print("~Slekkur~")
        kONni = False