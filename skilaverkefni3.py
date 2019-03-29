# Ragnar Helgi Breiðfjörð Unnþórsson
# 3/1/2019
# Skilaverkefni 3

import random

#Prentar dansara, prentar alla hluti nema seinasta(númer sex) með kommu á milli og síðan prentar það seinasta(númer sex)
def prentTuple(tup):
    for i in tup[:5]:
        print(end=i+', ')
    print(tup[5])
#Parar dönsurunum saman, tekur inn tup1 og tup2 setur lenið af tup1 í for lykkju og prentar tup1 og tup2 saman
def paraRod(tup1, tup2):
    for i in range(len(tup1)):
        print(tup1[i], "og", tup2[i])
#Para tvö random saman, tekur inn tup1 og tup2 setur lenið af tup1 í for lykkju og prentar tup1 og tup2 saman
def paraRandom(tup1, tup2):
    kk = random.sample(tup1, len(tup1))
    kvk = random.sample(tup2, len(tup2))
    for i in range(len(kk)):
        print(kk[random.randint(0, len(kk) - 1)], "og", kvk[random.randint(0, len(kvk) - 1)])
#Para tvö random saman, tekur inn tup1 og tup2 setur lenið af tup2 í for lykkju og prentar tup1 og tup2 saman
def paraRandomStakur(tup1, tup2):
    d = random.sample(tup2, len(tup2))
    for i in tup1:
        print(i, "og", d[random.randint(0, len(d) - 1)])
#Finnur staf í nöfnunum hjá dönsurunum, tekur inn staf frá notanda sem er settur í upper(s) og lower(b) og fer í for lykkju sem sér hvort að eitthvað nafn inniheldur stafin og ef svo tekur það nafnið og setur það í lista og prentar hann út í lokinn
def finnaStaf(tup1, tup2):
    s = input("Stafur: ").upper()
    b = s.lower()
    for i in list(tup1+tup2):
        if i.find(s) > -1 or i.find(b) > -1: print(i, end=', ')
    print()
#Finnur nöfn með upphafsstaf frá notandanum, setur tup1 og tup2 í for lykkju og ef fyrsti stafurinn í nafni er stafur sláður inn af notandanum setur forritið það í lista og prentar hann út í lokinn
def upphafsStafur(tup1, tup2):
    listi = []
    stafur = input("Sláðu inn staf: ").upper()
    for x in list(tup1+tup2):
        if x[0] == stafur: listi.append(x)
    for x in listi[:-1]: print(x, end=", ")
    print(listi[-1])
#Sér hvort að það eru tvö 'n' í nöfnunum, fer í for lykkju og sér hvort að það eru meira enn eitt 'n' og ef svo setur það nafnið í lista og prentar það
def tvoN(tup1, tup2):
    listi = []
    for x in list(tup1+tup2):
        if x.count('n') + x.count('N') > 1: listi.append(x)
    for x in listi[:-1]: print(x, end=", ")
    print(listi[-1])

def leitaSimaskra(nafn, dict):
    for x in dict:
        if x.lower() == nafn.lower(): print(x,"=",dict[x])

def prentDict(dict):
    for x in dict: print(x, dict[x], "ára")

def nsfw(dict):
    for x in dict:
        if int(dict[x]) >= 18: print(x, dict[x], "ára")

def medalAldur(dict):
    s = 0
    for x in dict:
        s += int(dict[x])
    print(s/len(dict))

def heildarAldur(dict):
    svar = 0
    for x in dict:
        svar += int(dict[x])
    print(svar)

def upphafsStafurDict(dict):
    listi = []
    stafur = input("Stafur: ").upper()
    for key, value in dict.items():
        if key[0] == stafur:
            listi.append(key)
            print(key, "er", value, "ára")
    return listi

def medalAldurDict(dict, list):
    result = 0
    for key, value in dict.items():
        for item in list:
            if key == item:
                result += int(value)
    print("Meðalaldur: " + str(result/len(dict)))

while True:
    print("1 - Dansarar")
    print("2 - Símaskrá")
    print("3 - Skráning í bekk")
    print("4 - Hætta")
    val = int(input("Val: "))
    if val == 1:
        while True:
            dansH = ('Björn', 'Bjarki', 'Bolli', 'Böðvar', 'Baldvin', 'Bergsteinn')
            dansD = ('Birta', 'Bryndís', 'Bergrún', 'Bríet', 'Birgitta', 'Bára')
            print("1 - Prenta dansara")
            print("2 - Para saman")
            print("3 - Para random")
            print("4 - Para random staka")
            print("5 - Finna staf")
            print("6 - Finna nafn með upphafsstaf")
            print("7 - Tvö 'n'")
            print("8 - Hætta")
            val1 = int(input("Val: "))
            if val1 == 1:
                print(end="Herrarnir: ")
                prentTuple(dansH)
                print(end="Dömurnar: ")
                prentTuple(dansD)

            elif val1 == 2: paraRod(dansH, dansD)

            elif val1 == 3: paraRandom(dansH, dansD)

            elif val1 == 4: paraRandomStakur(dansH, dansD)

            elif val1 == 5: finnaStaf(dansH, dansD)

            elif val1 == 6: upphafsStafur(dansH, dansD)

            elif val1 == 7: tvoN(dansH, dansD)

            elif val1 == 8: break

            else: print("~Villa~")


    elif val == 2:
        simaskra = {
            'Ragnar':'8488821',
            'Kormákur':'8884884',
            'Benni':'8739448',
            'Jakob':'8687337',
            'Páll':'8264274',
            'Margrét':'5478347',
            'Ásgeir':'8429559',
            'Óskar':'5613273',
            'Leifur':'5812345',
            'Ægir':'8624363'
        }
        leitaSimaskra(input("Nafn: "),simaskra)

    elif val == 3:
        while True:
            bekkur = {
                    'Bjarki':'16',
                    'Hrefna':'16',
                    'Kristín':'19',
                    'Alexander':'17',
                    'Hildur':'19',
                    'Kalli':'18',
                    'Greta':'16',
                    'Örn':'19',
                    'Perla':'15',
                    'Sófus':'18',
                    'Kjartanía':'16',
                    'Haraldur':'20',
                    'Helena':'16',
                    'Unnar':'17',
                    'Lilja':'16'
            }
            print("1 - Skrifa út alla nemendur")
            print("2 - Eldri enn 18")
            print("3 - Meðal aldur")
            print("4 - Heildar aldur")
            print("5 - Upphafstafur og meðalaldur")
            print("6 - Hætta")
            val3 = int(input("Val: "))
            if val3 == 1: prentDict(bekkur)

            elif val3 == 2: nsfw(bekkur)

            elif val3 == 3: medalAldur(bekkur)

            elif val3 == 4: heildarAldur(bekkur)

            elif val3 == 5:
                listi = upphafsStafurDict(bekkur)
                medalAldurDict(bekkur, listi)

            elif val3 == 6: break

            else: print("~Villa~")

    elif val == 4: break

    else: input("~Villa~")