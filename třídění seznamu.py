def trideni_seznamu():
    seznam = input("Zadejte čísla oddělená čárkami: ")
    seznam = [int(x) for x in seznam.split(",")]
    seznam.sort()
    print(f"Seřazený seznam: {seznam}")

trideni_seznamu()