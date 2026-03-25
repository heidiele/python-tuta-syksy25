import random

def noppa():
    return random.randint(1, 6)

#Main program
silmaluku = 0

while silmaluku != 6:
    silmaluku = noppa()
    print("Heiton tulos:", silmaluku)

