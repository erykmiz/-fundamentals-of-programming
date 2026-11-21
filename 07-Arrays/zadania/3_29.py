# Zadanie 3.29. Wypisujemy przykładową tablicę liczb w dwóch wierszach i czterech kolumnach.

numbers = [  # Tworzy tablicę składającą się z dwóch wierszy.
    [1, 2, 3, 4],  # Zapisuje cztery liczby w pierwszym wierszu.
    [5, 6, 7, 8],  # Zapisuje cztery liczby w drugim wierszu.
]  # Zamyka listę wierszy.

for row in numbers:  # Pobiera jeden wiersz w każdym obrocie pętli.
    print(*row)  # Przekazuje liczby z wiersza do print jako osobne argumenty oddzielone spacją.
