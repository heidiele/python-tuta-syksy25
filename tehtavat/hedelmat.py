#Hedelmähinnasto sanakirjana
hedelmat = {
    "omena" : 0.8,
    "banaani" : 1.2,
    "kiivi" : 2.5,
    "appelsiini" : 1.75
}

yhteishinta = 0

while True:
    h = input("Anna hedelmä jonka hinnan haluat tietää (tyhjä lopettaa): ")

    #Tyhjä lopettaa:
    if h == "":
        break

    if h in hedelmat:
        print(f"{h}n hinta on {hedelmat[h]} €/kg.")
        yhteishinta += hedelmat[h] #viittaamalla avaimeen h, saadaan lisättyä arvo eli kilohinta
    else:
        print(f"{h}lle ei löydy hintaa.")
        lisataanko = input("Haluatko lisätä hedelmän (Y/N)? ").upper()
        if lisataanko == "Y":
            hinta = float(input("Anna hinta euroina: "))
            hedelmat[h] = hinta
            yhteishinta += hinta
            print(f"{h} lisätty hinnalla {hinta} €")

#Tulostetaan yhteishinta
print(f"Yhteishinta on {yhteishinta} €")

#Tulostetaan päivitetty sanakirja
print("Päivitetty hinnasto:")
for nimi, hinta in hedelmat.items():
    print(f"{nimi}: {hinta} €")


