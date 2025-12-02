def summa(l):
    lukujen_summa = 0
    for luku in l:
        lukujen_summa += luku
    return lukujen_summa

#Main program
luvut = [5, 12, 3, 44, 8, 17, 0]
print("Lista:", luvut)

tulos = summa(luvut)
print("Lukujen summa on", tulos)