# Zadanie 2.6. Zmieniamy zera na jedynki na głównej przekątnej macierzy.

matrix = [  # Tworzy macierz 3 na 3 wypełnioną zerami.
    [0, 0, 0],  # Pierwszy wiersz macierzy.
    [0, 0, 0],  # Drugi wiersz macierzy.
    [0, 0, 0],  # Trzeci wiersz macierzy.
]  # Zamyka listę wierszy.

for index in range(len(matrix)):  # Przechodzi po indeksach od zera do ostatniego wiersza.
    matrix[index][index] = 1  # Ustawia jedynkę, gdy indeks wiersza i kolumny jest taki sam.

for row in matrix:  # Pobiera po jednym wierszu gotowej macierzy.
    print(*row)  # Rozpakowuje wiersz na osobne wartości i wyświetla je ze spacjami.
