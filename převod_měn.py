def currency_converter():
    rate = 0.041  # Předpokládaný kurz CZK na EUR
    czk = float(input("Zadejte částku v CZK: "))
    eur = czk * rate
    print(f"{czk} CZK je přibližně {eur:.2f} EUR.")

currency_converter()