import random

otazky = [
    {"otazka": "Kolik je 2 + 2?", "odpoved": "4"},
    {"otazka": "Jaké je hlavní město ČR?", "odpoved": "Praha"},
    {"otazka": "Kolik měsíců má rok?", "odpoved": "12"},
]

def spust_kviz():
    skore = 0
    nahodne_otazky = random.sample(otazky, len(otazky))

    for otazka in nahodne_otazky:
        odpoved = input(otazka["otazka"] + " ")
        if odpoved.lower() == otazka["odpoved"].lower():
            print("Správně!")
            skore += 1
        else:
            print("Špatně. Správná odpověď byla:", otazka["odpoved"])

    print(f"\nTvůj výsledek: {skore}/{len(otazky)}")

spust_kviz()
