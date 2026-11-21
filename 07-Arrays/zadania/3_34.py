# Zadanie 3.34. Zamieniamy pierwszy i ostatni wiersz tablicy 3 na 5.

numbers = [  # Tworzy przykładową tablicę trzech wierszy i pięciu kolumn.
    [1, 2, 3, 4, 5],  # Zapisuje pierwszy wiersz.
    [6, 7, 8, 9, 10],  # Zapisuje środkowy wiersz.
    [11, 12, 13, 14, 15],  # Zapisuje ostatni wiersz.
]  # Zamyka listę wierszy.

print('Before swapping rows:')  # Wprowadza wydruk początkowej tablicy.
for row in numbers:  # Przechodzi po wierszach przed zmianą.
    print(*row)  # Wypisuje elementy jednego wiersza.

numbers[0], numbers[-1] = numbers[-1], numbers[0]  # Pobiera oba wiersze i wpisuje je w odwrotnej kolejności.

print('After swapping rows:')  # Wprowadza wydruk tablicy po zmianie.
for row in numbers:  # Przechodzi po wierszach po zamianie.
    print(*row)  # Wypisuje elementy jednego wiersza po zmianie.
