# Zadanie 3.6. Znajdujemy minimum i maksimum przez porównywanie elementów.

numbers = [-15, 8, -31, 47, -2, 19]  # Zapisuje podane liczby dodatnie i ujemne.
maximum = numbers[0]  # Przyjmuje pierwszy element za dotychczasową największą wartość.
minimum = numbers[0]  # Przyjmuje ten sam element za dotychczasową najmniejszą wartość.
for number in numbers[1:]:  # Sprawdza pozostałe elementy, zaczynając od indeksu 1.
    if number > maximum:  # Sprawdza, czy bieżąca liczba jest większa od zapamiętanej.
        maximum = number  # Zapamiętuje nową największą liczbę.
    if number < minimum:  # Sprawdza, czy bieżąca liczba jest mniejsza od zapamiętanej.
        minimum = number  # Zapamiętuje nową najmniejszą liczbę.
print('Maximum:', maximum)  # Wyświetla największą liczbę, czyli 47.
print('Minimum:', minimum)  # Wyświetla najmniejszą liczbę, czyli -31.
