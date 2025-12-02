nimilista = set()

while True:
    nimi = input("Anna nimi, niin lisään sen listalle. (tyhjä lopettaa): ")
    if nimi == "":
        break
    if nimi in nimilista:
        print("Nimi on jo syötetty.")
    else:
        print("Uusi nimi lisätty.")
        nimilista.add(nimi)

print("Nimet listalla ovat:")
for nimet in nimilista:
    print(nimet)