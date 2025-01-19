def kalkulacka():
    a = float(input("Zadejte první číslo: "))
    b = float(input("Zadejte druhé číslo: "))
    operace = input("Zadejte operaci (+, -, *, /): ")

    if operace == '+':
        print(f"Výsledek: {a + b}")
    elif operace == '-':
        print(f"Výsledek: {a - b}")
    elif operace == '*':
        print(f"Výsledek: {a * b}")
    elif operace == '/':
        if b != 0:
            print(f"Výsledek: {a / b}")
        else:
            print("Chyba: Dělení nulou!")
    else:
        print("Neplatná operace!")

kalkulacka()