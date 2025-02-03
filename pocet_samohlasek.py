def pocet_samohlasek(text):
    samohlasky = "aeiouyáéíóúýěů"
    pocet = sum(1 for znak in text.lower() if znak in samohlasky)
    return pocet

text = input("Zadej text: ")
print("Počet samohlásek:", pocet_samohlasek(text))
