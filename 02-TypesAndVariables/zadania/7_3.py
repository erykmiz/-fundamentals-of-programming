# Zadanie 7.3: sprawdzenie, czy liczba jest parzysta.
# Przykłady: 24 -> True, 8 -> True, 31 -> False, 5 -> False.

number = int(input('Enter number: '))  # Wczytuje liczbę całkowitą z klawiatury.
even = number % 2 == 0  # Sprawdza, czy reszta z dzielenia liczby przez 2 wynosi 0.
print(f'Number is even: {even}')  # Wyświetla True dla liczby parzystej albo False dla nieparzystej.
