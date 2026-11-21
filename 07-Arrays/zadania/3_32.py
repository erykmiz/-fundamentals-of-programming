# Zadanie 3.32. Zastępujemy zera w tablicy 5 na 5 wynikami mnożenia.

table = [  # Zapisuje pięć osobnych wierszy po pięć zer.
    [0, 0, 0, 0, 0],  # Pierwszy wiersz.
    [0, 0, 0, 0, 0],  # Drugi wiersz.
    [0, 0, 0, 0, 0],  # Trzeci wiersz.
    [0, 0, 0, 0, 0],  # Czwarty wiersz.
    [0, 0, 0, 0, 0],  # Piąty wiersz.
]  # Zamyka listę wierszy.

for row_index in range(len(table)):  # Przechodzi po indeksach wierszy od 0 do 4.
    for column_index in range(len(table[row_index])):  # Odczytuje indeksy kolumn bieżącego wiersza.
        table[row_index][column_index] = (row_index + 1) * (column_index + 1)  # Zamienia indeksy na liczby od 1 do 5 i zapisuje ich iloczyn.

for row in table:  # Pobiera kolejny wiersz tabliczki mnożenia.
    formatted = [f'{value:2d}' for value in row]  # Rezerwuje po dwie pozycje na każdą liczbę, aby wyrównać kolumny.
    print(' '.join(formatted))  # Wypisuje wyrównane wartości oddzielone spacjami.
