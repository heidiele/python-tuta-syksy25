def kuusi(koko):
    print("Tämä on kuusi!")

    for i in range(koko):
        valit = koko - i - 1
        tahdet = 2 * i + 1
        print(" " * valit + "*" * tahdet)

    print(" " * (koko - 1) + "*")


#Pääohjelma
kuusi(5)