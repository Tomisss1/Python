def konvertuj_teplotu(c):
    return (c * 9/5) + 32

def konvertuj_delu_km_na_mile(km):
    return km * 0.621371

def konvertuj_vahu(kg):
    return kg * 2.20462

print("Jednotkový konvertor:")
print("1 - Teplota (°C na °F)")
print("2 - Délka (km na míle)")
print("3 - Váha (kg na libry)")

volba = input("Vyber možnost: ")

if volba == "1":
    c = float(input("Zadej teplotu v °C: "))
    print(f"{c} °C = {konvertuj_teplotu(c)} °F")
elif volba == "2":
    km = float(input("Zadej vzdálenost v km: "))
    print(f"{km} km = {konvertuj_delu_km_na_mile(km)} mil")
elif volba == "3":
    kg = float(input("Zadej váhu v kg: "))
    print(f"{kg} kg = {konvertuj_vahu(kg)} lb")
else:
    print("Neplatná volba")
