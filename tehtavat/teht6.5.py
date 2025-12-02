def parilliset(l):
    uusi_lista = []
    for luku in l:
        if luku % 2 == 0:
            uusi_lista.append(luku)
    return uusi_lista

#Pääohjelma
luvut = [5, 12, 3, 44, 8, 17, 0]
luvut2 = parilliset(luvut)

print("Alkuperäinen lista:", luvut)
print("Parillinen lista:", luvut2)