# Zadanie 3.8. Obliczamy średnią arytmetyczną za pomocą pętli while.

numbers = [15, 8, 31, 47, 2, 19]  # Zapisuje wszystkie wartości z polecenia.
index = 0  # Ustawia indeks na początek tablicy.
total = 0  # Ustawia sumę początkową na zero.
while index < len(numbers):  # Powtarza działania, dopóki indeks mieści się w tablicy.
    total += numbers[index]  # Dolicza liczbę znajdującą się pod bieżącym indeksem.
    index += 1  # Przechodzi do kolejnej pozycji.
average = total / len(numbers)  # Dzieli sumę przez liczbę elementów.
print('Array:', *numbers)  # Wyświetla liczby z tablicy oddzielone spacjami.
print('Arithmetic mean:', average)  # Wyświetla obliczoną średnią.
