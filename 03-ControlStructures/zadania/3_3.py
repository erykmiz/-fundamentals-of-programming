# Zadanie 3.3: zniżka dla osób poniżej 18 lat lub od 65 lat.

age = int(input('Enter your age: '))  # Pobiera wiek jako liczbę całkowitą.
if age < 18 or age >= 65:  # or wymaga choć jednego warunku: wiek poniżej 18 albo co najmniej 65.
    print('Discount is available')  # Pokazuje, że zniżka przysługuje.
else:  # Pozostają osoby w wieku od 18 do 64 lat.
    print('Discount is not available')  # Pokazuje, że zniżka nie przysługuje.
