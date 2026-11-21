# Zadanie 3.33. Szukamy najmniejszej i największej liczby oraz ich położenia.

numbers = [  # Zapisuje cztery wiersze tablicy z polecenia.
    [-38, 19],  # Pierwszy wiersz.
    [5, 40],  # Drugi wiersz.
    [-7, 11],  # Trzeci wiersz.
    [29, 16],  # Czwarty wiersz.
]  # Zamyka listę wierszy.

smallest = numbers[0][0]  # Za początkowe minimum przyjmuje pierwszy element.
largest = numbers[0][0]  # Ten sam element wykorzystuje jako początkowe maksimum.
smallest_row, smallest_column = 1, 1  # Zapisuje położenie minimum, licząc rzędy i kolumny od 1.
largest_row, largest_column = 1, 1  # Zapisuje początkowe położenie maksimum.

for row_number, row in enumerate(numbers, start=1):  # Pobiera każdy wiersz i jego numer od 1.
    for column_number, value in enumerate(row, start=1):  # Pobiera liczbę i numer jej kolumny od 1.
        if value < smallest:  # Sprawdza, czy bieżąca liczba jest mniejsza od znalezionego minimum.
            smallest = value  # Zapamiętuje nową najmniejszą wartość.
            smallest_row, smallest_column = row_number, column_number  # Zapamiętuje jej wiersz i kolumnę.
        if value > largest:  # Sprawdza, czy bieżąca liczba jest większa od znalezionego maksimum.
            largest = value  # Zapamiętuje nową największą wartość.
            largest_row, largest_column = row_number, column_number  # Zapamiętuje jej wiersz i kolumnę.

print(f'Smallest: {smallest} (row {smallest_row}, column {smallest_column})')  # Wypisuje minimum wraz z położeniem.
print(f'Largest: {largest} (row {largest_row}, column {largest_column})')  # Wypisuje maksimum wraz z położeniem.
