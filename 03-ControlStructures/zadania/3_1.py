# Zadanie 3.1: przykłady operatorów logicznych and, or i not.
has_ticket = True  # Przyjmuje, że przykładowa osoba ma bilet.
has_id = False  # Przyjmuje, że przykładowa osoba nie ma dokumentu.
print(has_ticket and has_id)  # and wymaga obu wartości True; tutaj wynik to False.
print(has_ticket or has_id)  # or wymaga przynajmniej jednej wartości True; tutaj wynik to True.
print(not has_ticket)  # not odwraca wartość logiczną; z True otrzymuje False.
