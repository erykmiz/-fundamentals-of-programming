# Zadanie 3.14. Wypisujemy wartości, które występują w tablicy dokładnie raz.

numbers = [2, 3, 2, 5, 8, 1, 9, 8]  # Zapisuje przykładową tablicę z polecenia.
unique = []  # Tworzy listę na wartości występujące tylko raz.
for number in numbers:  # Pobiera liczby w kolejności z tablicy.
    if numbers.count(number) == 1:  # Sprawdza, czy bieżąca wartość ma dokładnie jedno wystąpienie.
        unique.append(number)  # Zachowuje wartość spełniającą warunek.
print('Array:', *numbers)  # Wyświetla zawartość przykładowej tablicy.
print('Unique elements:', *unique)  # Wyświetla wartości 3, 5, 1 i 9 w kolejności ich wystąpienia.
