#Ragnar Helgi Breiðfjörð Unnþórsson
def geraLista():
    l = []
    for x in range(2, 1001, 2):
        l.append(x)
    return(l)

def skrifaiSkra(l, nafntxt):
    skra = open(nafntxt, 'w', encoding='utf-8')
    for x in l:
        skra.write(str(x)+" ")
    skra.close()

def lesaiSkra(l, nafntxt):
    skra = open(nafntxt, 'r', encoding='utf-8')
    listi = skra.read().split(" ")
    skra.close()
    print(listi)

def prenta(listi):
    for k in listi[::-1]: print(k, end=", ")
    print(listi[-1])

def lesaSkra(nafntxt):
    skra = open(nafntxt, 'r', encoding='utf-8')
    listi = skra.read().split(" ")
    skra.close()
    listi.pop()
    listi = list(map(int, listi))
    return listi


def primtolur():
    listi = []
    for n in range(1, 101):
        if n > 1:
            for i in range(2, n):
                if (n%i) == 0: break
            else: listi.append(n)
    return listi

def finnaFjordu():
    temp = []
    for x in range(0, len(listi), 4):
        temp.append(x)
    return temp

def skrifaSkraTuple(tup, nafntxt):
    skra = open(nafntxt, 'w' , encoding='utf-8')
    skra.write(tup + " ")
    skra.close()


while True:
    print("1 - Sléttar tölur")
    print("2 - Prímtölur")
    print("3 - ")
    print("4 - ")
    print("5 - Hætta")
    konni = int(input("Val: "))
    if konni == 1:
        while True:
            print("1 - Skrifa skrá")
            print("2 - Lesa í skrá")
            val = int(input("Val: "))
            if val == 1:
                listi = geraLista()
                tup = tuple(listi)
                skrifaiSkra(listi, 'nafn.txt')

            elif val == 2:
                listi = geraLista()
                lesaiSkra(listi, 'nafn.txt')

            elif val == 3:
                lesaSkra('nafn.txt')

            elif val == 4:
                listi = geraLista()
                prenta(listi)

            elif val == 5:
    elif konni == 2:
        listi = primtolur()
        skrifaiSkra(listi, 'primtolur.txt')
        primToluListi = lesaSkra(listi, 'primtolur.txt')

    elif konni == 3:
        tup1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        tup2 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
        tup3 = ('"konni"', 123, '"sponni"', 234)
        skrifaSkraTuple(tup1, 'tupleskra.txt')
        skrifaSkraTuple(tup2, 'tupleskra.txt')
        skrifaSkraTuple(tup3, 'tupleskra.txt')



    elif konni == 5: break