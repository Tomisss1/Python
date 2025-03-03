def kg_na_libry(kg):
    return kg * 2.20462

def libry_na_kg(libry):
    return libry / 2.20462

volba = input("Zadejte '1' pro převod kg na libry nebo '2' pro převod liber na kg: ")

if volba == '1':
    kg = float(input("Zadejte hmotnost v kilogramech: "))
    print(f"{kg} kg je {kg_na_libry(kg)} liber.")
elif volba == '2':
    libry = float(input("Zadejte hmotnost v librách: "))
    print(f"{libry} liber je {libry_na_kg(libry)} kg.")
else:
    print("Neplatná volba!")
    