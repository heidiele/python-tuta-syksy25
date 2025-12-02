#Sanakirja, jossa avain = ICAO-koodi ja arvo = lentoaseman nimi
lentoasemat = {
    "EFHK" : "Helsinki-Vantaa",
    "JHKY" : "Dubai",
    "KERF" : "Oslo"
}

while True:
    print("Valitse toiminto: A = SYÖTÄ, B = HAE ja Q = LOPETA: ")

    valinta = input("Mitä haluat tehdä: ").upper()

    if valinta == "A":
        icao = input("Anna lentoaseman ICAO koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Uusi arvo tallennettu.")

    elif valinta == "B":
        icao = input("Anna lentoaseman ICAO-koodi: ")
        if icao in lentoasemat:
            print("Lentoaseman nimi:", lentoasemat[icao])
        else:
            print("Koodilla ei löydy nimeä.")

    elif valinta == "Q":
        print("Ohjelma päättyy...")
        break

    else:
        print("Virheellinen valinta.")

print("Kiitos, hei!")
