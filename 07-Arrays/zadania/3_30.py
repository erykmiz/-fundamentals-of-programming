# Zadanie 3.30. Sumujemy liczby z ostatniej kolumny tablicy.

numbers = [  # Zapisuje cztery wiersze tablicy z polecenia.
    [7, 3, 7, 9, 0],  # Pierwszy wiersz kończy się liczbą 0.
    [2, 9, 0, 1, 5],  # Drugi wiersz kończy się liczbą 5.
    [3, 8, 6, 4, 7],  # Trzeci wiersz kończy się liczbą 7.
    [8, 7, 1, 1, 5],  # Czwarty wiersz kończy się liczbą 5.
]  # Zamyka listę wierszy.

total = 0  # Ustawia sumę początkową na zero.
for row in numbers:  # Odczytuje kolejno wszystkie wiersze.
    total += row[-1]  # Dodaje ostatni element wiersza, dostępny pod indeksem -1.
print('Sum of the last column:', total)  # Wyświetla sumę ostatniej kolumny, czyli 17.
