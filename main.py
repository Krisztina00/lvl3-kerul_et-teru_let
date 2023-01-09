from szamitas import Szamitas
from nyomtat import Nyomtat
nev = input("Név : ")
input_num1 = input("szam1 : ")
input_num2 = input("szam2 : ")
input_num3 = input("szam3 : ")

if input_num1.isnumeric() and input_num2.isnumeric() and input_num3.isnumeric():
    num1 = int(input_num1)
    num2 = int(input_num2)
    num3 = int(input_num3)

    nyom = Nyomtat(nev,num1,num2,num3)
    nyom.nyomatos_metodus()

    szamolas = Szamitas(num1,num2,num3)
    szamolas.szamol()
    print(szamolas.kerulet)
    print(szamolas.terulet)
else:
    print("nem szam")