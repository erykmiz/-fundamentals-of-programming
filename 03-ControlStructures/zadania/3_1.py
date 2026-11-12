# Zadanie 3.1: przykłady operatorów logicznych and, or i not.

has_ticket = True  # Zapisuje True, czyli osoba ma bilet.
has_id = False  # Zapisuje False, czyli osoba nie ma dokumentu.
print(has_ticket and has_id)  # and wymaga obu True; tutaj pokazuje False.
print(has_ticket or has_id)  # or wymaga choć jednego True; tutaj pokazuje True.
print(not has_ticket)  # not odwraca wartość True na False.
