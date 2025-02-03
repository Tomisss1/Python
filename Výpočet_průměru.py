cisla = input("Zadejte čísla oddělená čárkou: ")
cisla_list = [float(x) for x in cisla.split(',')]
prumer = sum(cisla_list) / len(cisla_list)
print("Průměr je:", prumer)
