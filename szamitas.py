class Szamitas:
    #konstruktor = def inites
    def __init__(self, a , b, c):
        self.kerulet = 0
        self.terulet=0
        self.a = a
        self.b = b
        self.c = c

    def szamol(self):
        self.kerulet= self.a + self.b + self.c
        self.terulet = (self.a * self.b)/2