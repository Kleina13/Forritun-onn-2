#annar klassi
class Reikna():
    def __init__(self, t1, t2):
        self.tala1 = t1
        self.tala2 = t2

    def samlagning(self):
        return self.tala1 + self.tala2
    def margfoldun(self):
        return self.tala1 * self.tala2
    def bil(self):
        for x in range(self.tala1, self.tala2):
            print(x)

r1 = Reikna(2, 15)
r2 = Reikna(89, 200)
r3 = Reikna(777, 800)

r3.bil()