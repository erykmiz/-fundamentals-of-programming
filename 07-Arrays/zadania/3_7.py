# Zadanie 3.7. Obliczamy średnią arytmetyczną za pomocą pętli for.

numbers = [15, 8, 31, 47, 2, 19]  # Zapisuje wszystkie wartości z polecenia.
total = 0  # Ustawia sumę początkową na zero.
for number in numbers:  # Pobiera każdą wartość z tablicy po kolei.
    total += number  # Dodaje bieżącą wartość do sumy.
average = total / len(numbers)  # Dzieli sumę przez liczbę elementów.
print('Array:', *numbers)  # Wyświetla liczby z tablicy oddzielone spacjami.
print('Arithmetic mean:', average)  # Wyświetla obliczoną średnią.
