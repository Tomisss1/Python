import random

tajne_cislo = random.randint(1, 100)
pokus = 0

while True:
    hadane_cislo = int(input("Hádej číslo mezi 1 a 100: "))
    pokus += 1

    if hadane_cislo < tajne_cislo:
        print("Zkus vyšší číslo.")
    elif hadane_cislo > tajne_cislo:
        print("Zkus nižší číslo.")
    else:
        print(f"Gratuluji! Uhodl jsi číslo {tajne_cislo} na {pokus}. pokus.")
        break
