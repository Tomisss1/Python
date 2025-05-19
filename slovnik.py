databaze = {}

def pridej_uzivatele(jmeno, vek):
    databaze[jmeno] = vek

def vypis_uzivatele():
    for jmeno, vek in databaze.items():
        print(f"{jmeno} je {vek} let starý/á.")

def najdi_uzivatele(jmeno):
    if jmeno in databaze:
        print(f"{jmeno} je {databaze[jmeno]} let starý/á.")
    else:
        print("Uživatel nenalezen.")

# Testování
pridej_uzivatele("Tomáš", 25)
pridej_uzivatele("Anna", 30)
vypis_uzivatele()
najdi_uzivatele("Tomáš")
