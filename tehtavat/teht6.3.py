# 1 gallona = 3.785 litraa

def muunnos(g):
    l = g * 3.785
    return l

#Main program
gallonat = float(input("Anna gallonien määrä, negatiivinen lopettaa: "))

while gallonat >= 0:
    litrat = muunnos(gallonat)
    print(f"Määrä litroina: {litrat:.3f}")
    gallonat = float(input("Anna gallonien määrä, negatiivinen lopettaa: "))

print("Kiitos hei!")