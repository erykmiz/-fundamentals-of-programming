# Zadanie 3.12. Wypisujemy wartości z pierwszej tablicy, których brakuje w drugiej.

first = [4, 36, 12, 28, 9, 44, 5]  # Zapisuje pierwszą tablicę z polecenia.
second = [5, 1, 36]  # Zapisuje drugą tablicę z polecenia.
difference = []  # Tworzy listę na liczby występujące tylko w pierwszej tablicy.
for number in first:  # Pobiera każdą liczbę z pierwszej tablicy.
    if number not in second:  # Sprawdza, czy drugiej tablicy brakuje tej liczby.
        difference.append(number)  # Dopisuje wartość do wyniku.
print(*difference)  # Wyświetla 4, 12, 28, 9 i 44 w kolejności z pierwszej tablicy.
