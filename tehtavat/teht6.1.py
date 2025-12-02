import random

def noppa(suurin):
    return random.randint(1, suurin)

#Main program
suurin = int(input("Kuinka suurta noppaa haluat heittää? "))
silmaluku = 0

while silmaluku != suurin:
    silmaluku = noppa(suurin)
    print("Heiton tulos:", silmaluku)

