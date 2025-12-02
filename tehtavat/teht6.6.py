import math

def yksikkohinta(halkasija, hinta):
    #lasketaan pizzan pinta-ala neliömetreinä
    sade = halkasija / 2
    pinta_ala = math.pi * (sade / 100) **2 #cm -> metreiksi
    #Yksikköhinta = €/nm2
    return hinta / pinta_ala

#Main program
halkasija1 = float(input("Halkaisija pizza1 (cm): "))
hinta1 = float(input("Hinta pizza1 (€): "))

halkasija2 = float(input("Halkaisija pizza2 (cm): "))
hinta2 = float(input("Hinta pizza2 (€): "))

#Lasketaan yksikköhinnat
pizza1 = yksikkohinta(halkasija1, hinta1)
pizza2 = yksikkohinta(halkasija2, hinta2)
print(f"Pizza 1 yksikköhinta on {pizza1:.2f} €/nm2")
print(f"Pizza 2 yksikköhinta on {pizza2:.2f} €/nm2")

#Verrataan
if pizza1 < pizza2:
    print("Ensimmäinen pizza on yksikköhinnaltaan halvempi.")
elif pizza2 < pizza1:
    print("Toinen pizza on yksikköhinnaltaan halvempi.")
else:
    print("Yksikköhinta on sama molemmilla pizzoilla.")