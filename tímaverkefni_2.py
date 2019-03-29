#Ragnar Helgi Breiðfjörð Unnþórsson

import csv

# LIÐUR 1
def lesaSkra(nafntxt):
    counter = 0
    lol = open(nafntxt, 'r', encoding='utf-8')
    lesari = csv.reader(lol, delimiter=",")
    for row in lesari:
        print(row, end=", ")
        counter += 1
        if counter == 3:
            print("\n")
            counter = 0

# LIÐUR 2
def prentaTuple(tup):
    counter = 1
    for x in tup:
        print(str(counter) + "=>", x)
        counter += 1
    print()

def fyrstiStafur(tup):
    listi = list(tup)
    stafur = input("Stafur: ").lower()
    for i in listi:
        if i[0] == stafur: print(i, end=" ")
    print()

# LIÐUR 3
def medaltalStafa(dict):
    stafaList = []
    svarList = []
    stafur = input("Stafur: ").lower()
    while stafur != "":
        stafaList.append(stafur)
        stafur = input("Stafur: ").lower()
    for x, y in dict.items():
        for i in stafaList:
            if i == y: svarList.append(x)
    return sum(svarList) / len(svarList)

def tolurNafn(dict, string):
    svar = []
    dot = csv.reader(string, delimiter=";")
    for s in dot:
        for x, y in dict.items():
            if str(x) == s: svar.append(y)
    return ''.join(svar)

while True:
    print("~Tímaverkefni 2~")
    print("1 - Liður 1")
    print("2 - Liður 2")
    print("3 - Liður 3")
    print("4 - Hætta")
    val = int(input("Val: "))
    print()

    if val == 1:
        name = 'skr.txt'
        skra = open(name, 'w', encoding='utf-8')
        skra.write('152,235,540,4566,5666,6766567,5,56,567')
        skra.close()
        while True:
            print("~Liður 1~")
            print("1 - Lesa skrá")
            print("2 - Summa fimm")
            print("3 - Hætta")
            konni = int(input("Val: "))
            print()

            if konni == 1: lesaSkra(name)

            elif konni == 2: pass

            elif konni == 3: break

    elif val == 2:
        veididot = ('veiðistöng', 'fluga', 'veiðihjól', 'stígvél', 'taska', 'háfur')
        prentaTuple(veididot)
        fyrstiStafur(veididot)
        print()

    elif val == 3:
        stafrof = {
            1:'a',
            2:'b',
            3:'d',
            4:'e',
            5:'f',
            6:'g',
            7:'h',
            8:'i',
            9:'j',
            10:'k',
            11:'l',
            12:'m',
            13:'n',
            14:'o',
            15:'p',
            16:'r',
            17:'s',
            18:'t',
            19:'u',
            20:'v',
            21:'y',
            22:' '
        }
        print("Meðaltal stafana er", medaltalStafa(stafrof))
        print(tolurNafn(stafrof, '10;14;13;13;8'))
        print()

    elif val == 4: break