# Zadanie 3.37. Transponujemy macierze, czyli zamieniamy ich kolumny na wiersze.

def transpose_matrix(m):  # Przyjmuje prostokątną macierz zapisaną jako lista wierszy.
    if not m:  # Sprawdza, czy macierz nie zawiera żadnego wiersza.
        return []  # Zwraca pustą listę, bo nie ma kolumn do przełożenia.
    transposed = []  # Przygotowuje listę wierszy nowej macierzy.
    for column_index in range(len(m[0])):  # Przechodzi po indeksach kolumn pierwotnej macierzy.
        new_row = []  # Przygotowuje wiersz z wartościami z bieżącej kolumny.
        for row in m:  # Pobiera każdy wiersz pierwotnej macierzy.
            new_row.append(row[column_index])  # Dodaje element bieżącej kolumny z pobranego wiersza.
        transposed.append(new_row)  # Dopisuje ukończony wiersz do nowej macierzy.
    return transposed  # Zwraca macierz o zamienionych wymiarach.


if __name__ == '__main__':  # Uruchamia przykłady po bezpośrednim otwarciu pliku.
    matrices = [  # Zapisuje trzy przykładowe macierze.
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # Pierwsza macierz ma trzy wiersze i trzy kolumny.
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]],  # Druga macierz ma dwa wiersze i pięć kolumn.
        [[5, 6, 7, 8]],  # Trzecia macierz ma jeden wiersz i cztery kolumny.
    ]  # Zamyka listę macierzy.
    for number, matrix in enumerate(matrices, start=1):  # Pobiera każdą macierz i numer przykładu.
        print(f'Transposed matrix {number}:')  # Wypisuje nagłówek bieżącego przykładu.
        for row in transpose_matrix(matrix):  # Pobiera kolejne wiersze macierzy po transpozycji.
            print(*row)  # Wypisuje wartości jednego wiersza od lewej do prawej.
