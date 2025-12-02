import random
def noppa():
    eka = random.randint(1, 6)
    toka = random.randint(1, 6)
    return eka, toka

noppa1, noppa2 = noppa()
print(f"Nopista tuli {noppa1} ja {noppa2}.")

