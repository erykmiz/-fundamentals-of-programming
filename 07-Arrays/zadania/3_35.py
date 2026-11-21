# Zadanie 3.35. Zamieniamy pierwszą i ostatnią kolumnę tablicy 3 na 5.

numbers = [  # Tworzy przykładową tablicę trzech wierszy i pięciu kolumn.
    [1, 2, 3, 4, 5],  # Zapisuje pierwszy wiersz.
    [6, 7, 8, 9, 10],  # Zapisuje drugi wiersz.
    [11, 12, 13, 14, 15],  # Zapisuje trzeci wiersz.
]  # Zamyka listę wierszy.

print('Before swapping columns:')  # Wprowadza wydruk początkowej tablicy.
for row in numbers:  # Przechodzi po wierszach przed zmianą.
    print(*row)  # Wypisuje elementy jednego wiersza.

for row in numbers:  # Wykonuje zamianę w każdym wierszu.
    row[0], row[-1] = row[-1], row[0]  # Zamienia pierwszy i ostatni element bieżącego wiersza.

print('After swapping columns:')  # Wprowadza wydruk tablicy po zmianie.
for row in numbers:  # Przechodzi po wierszach po zamianie.
    print(*row)  # Wypisuje elementy jednego wiersza po zmianie.
