class Setning():
    def __init__(self, s):
        self.strengur = s
    def breyta_streng(self, new):
        self.strengur = new
    def __str__(self):
        return self.strengur

class Medlimir():
    def __init__(self, n, g, h, e):
        self.nafn = n
        self.gsm = g
        self.heimasimi = h
        self.email = e
    def breyta_nafn(self, new):
        self.nafn = new
    def breyta_gsm(self, new):
        self.gsm = new
    def breyta_heimasimi(self, new):
        self.heimasimi = new
    def breyta_email(self, new):
        self.email = new
    def __str__(self):
        return "Nafn: " + str(self.nafn) + ". GSM: " + str(self.gsm) + ". Heimasímí: " + str(self.heimasimi) + ". Email: " +str(self.email)

class Nemendur():
    def __init__(self, n, a, b):
        self.nafn = n
        self.aldur = a
        self.braut = b
    def elsti_nem(listi):
        aldur = 0
        nafn = ''
        for x in listi:
            if x.aldur > aldur:
                aldur = x.aldur
                nafn = x.nafn
        print("Elsti nemi er ", nafn, " hann er ", aldur, " ára.")

while True:
    print("1 - Setning")
    print("2 - Meðlimir")
    print("3 - Nemendur")
    print("4 - Bankareikningur")
    print("5 - Hætta")
    val = int(input("Hvað viltu gera: "))
    if val == 1: print(Setning(input("Hvað viltu prenta út: ")))
    elif val == 2: print(Medlimir(input("Nafn: "), input("GSM: "), input("Heimasími: "), input("Email: ")))
    elif val == 3:
        n1 = Nemendur('Ragnar', 16, 'Tölvubraut')
        n2 = Nemendur('Jóakim', 21, 'Hárgreiðslubraut')
        n3 = Nemendur('Gunnar', 17, 'Tölvubraut')
        n4 = Nemendur('Aðólf', 6, 'K2')
        n5 = Nemendur('Ragnar2', 16, 'Tölvubraut')
        nemlisti = [n1, n2, n3, n4, n5]
        Nemendur.elsti_nem(nemlisti)

    elif val == 5: break