# Zadanie 3.4. Wypisujemy elementy tablicy w odwrotnej kolejności.

numbers = [15, 8, 31, 47, 2, 19]  # Zapisuje liczby w kolejności z polecenia.
reversed_numbers = []  # Tworzy pustą listę na wynik.
for index in range(len(numbers) - 1, -1, -1):  # Schodzi od ostatniego indeksu do 0, pomijając granicę -1.
    reversed_numbers.append(numbers[index])  # Dopisuje element spod bieżącego indeksu.
print('existed array:', *numbers)  # Gwiazdka przekazuje elementy osobno, więc print oddziela je spacją.
print('reverse array:', *reversed_numbers)  # Wyświetla wartości od ostatniej do pierwszej.
