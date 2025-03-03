heslo = input("Zadejte heslo: ")

if len(heslo) >= 8 and any(c.isupper() for c in heslo) and any(c.islower() for c in heslo) and any(c.isdigit() for c in heslo):
    print("Heslo splňuje požadavky.")
else:
    print("Heslo nesplňuje požadavky.")
    