from szamitas import Szamitas
import datetime

class Nyomtat:
    def __init__(self, nev, a,b,c):
        self.nev = nev
        self.a = a
        self.b = b
        self.c = c
    
    def nyomatos_metodus(self):
        szamolas = Szamitas(self.a,self.b,self.c)
        szamolas.szamol()
        print(szamolas.kerulet)
        print(szamolas.terulet)
        datum = datetime.datetime.now().strftime("%m.%d.%y")

        f = open("kisztina_kalapacs.txt", "w")
        f.write("szamitasos lap")
        f.write(f"felhasznalo neve: {self.nev}")
        f.write(f"a oldal: {self.a}")
        f.write(f"a oldal: {self.b}")
        f.write(f"a oldal: {self.c}")
        f.write(f" kerulet : {szamolas.terulet}")
        f.write(f"terulet : {szamolas.terulet}")
        f.write("\n")
        f.write(f"kelt: szeged , {datum}")

        f.close()
