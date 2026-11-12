# Zadanie 1.6: liczba parzysta lub nieparzysta.

number = int(input('Enter number: '))  # Pobiera liczbę całkowitą z klawiatury.
if number % 2 == 0:  # % liczy resztę; reszta 0 z dzielenia przez 2 oznacza liczbę parzystą.
    print(f'{number} is even')  # f wstawia liczbę w miejsce {number} i pokazuje, że jest parzysta.
else:  # Wybiera tę część, gdy liczba nie jest parzysta.
    print(f'{number} is odd')  # Pokazuje, że podana liczba jest nieparzysta.
