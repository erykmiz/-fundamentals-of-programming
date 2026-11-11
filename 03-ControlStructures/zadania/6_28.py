# Zadanie 6.28: pierwsze dwadzieścia wyrazów ciągu Fibonacciego.
first = 0  # Zapisuje pierwszy wyraz ciągu.
second = 1  # Zapisuje drugi wyraz ciągu.
for index in range(20):  # Powtarza wypisanie wyrazu i przesunięcie pary dokładnie 20 razy.
    print(first, end=' ')  # Wyświetla bieżący wyraz ze spacją zamiast nowej linii.
    next_number = first + second  # Oblicza następny wyraz jako sumę dwóch dotychczasowych.
    first = second  # Przesuwa drugi wyraz na miejsce pierwszego.
    second = next_number  # Zapisuje obliczony następny wyraz jako drugi element pary.
print()  # Kończy linię po dwudziestu liczbach.
