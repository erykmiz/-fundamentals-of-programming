# Zadanie 3.3. Liczymy parzyste wartości w tablicy za pomocą pętli while.

numbers = [34, 7, 19, 4, 21, 8]  # Zapisuje liczby podane w poleceniu.
index = 0  # Zaczyna od indeksu pierwszego elementu.
even_count = 0  # Ustawia licznik liczb parzystych na zero.
while index < len(numbers):  # Powtarza sprawdzanie, dopóki indeks wskazuje element listy.
    if numbers[index] % 2 == 0:  # Sprawdza, czy reszta z dzielenia bieżącej liczby przez 2 wynosi zero.
        even_count += 1  # Dolicza znalezioną liczbę parzystą.
    index += 1  # Przechodzi do następnego elementu bez względu na jego parzystość.
print('Number of even values:', even_count)  # Wyświetla liczbę elementów parzystych.
