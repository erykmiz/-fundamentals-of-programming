# Zadanie 3.22. Układamy parzyste liczby przed nieparzystymi.

arr = [7, 9, 2, 4, 5, 6]  # Tworzy listę z liczbami podanymi w poleceniu.
even_numbers = []  # Przygotowuje osobną listę dla liczb parzystych.
odd_numbers = []  # Przygotowuje osobną listę dla liczb nieparzystych.

for number in arr:  # Odczytuje liczby w ich początkowej kolejności.
    if number % 2 == 0:  # Sprawdza, czy reszta z dzielenia przez dwa wynosi zero.
        even_numbers.append(number)  # Dodaje liczbę parzystą na koniec pierwszej listy.
    else:  # Obsługuje liczbę o niezerowej reszcie.
        odd_numbers.append(number)  # Dodaje liczbę nieparzystą na koniec drugiej listy.

print('Before:', arr)  # Pokazuje kolejność liczb przed zmianą.
arr = even_numbers + odd_numbers  # Łączy listy tak, aby cała grupa liczb parzystych była na początku.
print('After:', arr)  # Pokazuje liczby po przestawieniu.
