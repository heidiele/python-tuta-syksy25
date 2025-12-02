#Funktio osallistujien laskemiseksi
def osallistujat(sanakirja):
    kurssi = input("Anna kurssin nimi, jonka osallistujamäärän haluat tietää: ")
    maara = 0

    for nimi, kurssit in sanakirja.items():
        if kurssi in kurssit:
            maara += 1

    return maara


oppilaat = {
    "Matti" : ["Englanti", "Matematiikka", "Historia"] ,
    "Heidi" : ["Liikunta", "Historia", "Fysiikka"],
    "Touko" : ["Englanti", "Biologia", "Liikunta"]
}

#Lisätään uusi oppilas ja kysytään kurssit
uusi = input("Anna oppilaan nimi: ")
kurssit = []
print("Anna seuraavaksi oppilaan kurssit:")

while True:
    kurssi = input("Anna seuraava kurssi: ")
    if kurssi == "":
        break
    kurssit.append(kurssi)

oppilaat[uusi] = kurssit

oppilasmaara = osallistujat(oppilaat)
print(f"Kurssille osallistuu {oppilasmaara} oppilasta.")

for n in oppilaat.items():
    print(n)

