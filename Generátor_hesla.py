import random
import string

def generuj_heslo(delka):
    znaky = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(znaky) for _ in range(delka))

delka = int(input("Zadej délku hesla: "))
print("Vygenerované heslo:", generuj_heslo(delka))