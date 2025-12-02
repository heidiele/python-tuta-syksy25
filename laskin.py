#Yhteenlasku
def summa(num1, num2):
    print("Yhteenlaskun tulos on:", num1 + num2)
    return

#Vähennyslasku
def vahennys(num1, num2):
    print("Vähennyslaskun tulos on:", num1 - num2)
    return

#Kertolasku
def kerto(num1, num2):
    print("Kertolaskun tulos on:", num1 * num2)
    return

#Jakolasku
def jako(num1, num2):
    if b != 0:
        print("Jakolaskun tulos on:", num1 / num2)
    else:
        print("Nollalla ei voi jakaa!")
    return

#Pääohjelma
print("-----Tervetuloa käyttämään laskinta!-----")

while True:
    print("\nValitse mitä toimintoa haluat käyttää:\n A: Yhteenlasku \n B: Vähennyslasku"
          "\n C: Kertolasku \n D: Jakolasku")

    valinta = input("Valintasi (A - D), Q lopettaa: ").upper()

    #While loopin katkaisu
    if valinta == "Q":
        print("Ohjelma lopetetaan, kiitos hei!")
        break

    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))

    if valinta == "A":
        summa(a, b)
    elif valinta == "B":
        vahennys(a, b)
    elif valinta == "C":
        kerto(a, b)
    elif valinta == "D":
        jako(a, b)
    else:
        print("Valintasi oli virheellinen.")
