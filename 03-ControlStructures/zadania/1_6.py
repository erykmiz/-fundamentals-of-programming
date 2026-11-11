# Zadanie 1.6: liczba parzysta lub nieparzysta.
number = int(input('Enter number: '))  # Pobiera liczbę całkowitą wpisaną z klawiatury.
if number % 2 == 0:  # Sprawdza, czy reszta z dzielenia przez 2 jest równa 0.
    print(f'{number} is even')  # Informuje, że liczba jest parzysta.
else:  # Wybiera tę część, gdy reszta z dzielenia przez 2 nie wynosi 0.
    print(f'{number} is odd')  # Informuje, że liczba jest nieparzysta.
