# Zadanie 1.4. Odczytujemy elementy listy przez ich indeksy.

arr = [2, 3, 7, 5, 4]  # Zapisuje liczby w kolejności podanej w poleceniu.
length = len(arr)  # Liczy elementy, aby użyć tej liczby przy wyznaczaniu indeksów.
print(arr)  # Wypisuje całą listę w nawiasach kwadratowych.
print('Number of elements', length)  # Pokazuje liczbę elementów listy.
print('First value', arr[0])  # Odczytuje pierwszy element o indeksie 0.
print('Second value', arr[1])  # Odczytuje drugi element o indeksie 1.
print('Last value', arr[length - 1])  # Odczytuje ostatni element, odejmując 1 od długości.
print('Last but one value', arr[length - 2])  # Odczytuje przedostatni element przez indeks dodatni.
print('Sum of first and last value', arr[0] + arr[length - 1])  # Dodaje elementy z obu końców listy.
print('Middle value', arr[length // 2])  # Dzieli długość całkowicie przez 2, aby znaleźć środkowy indeks.

for index in range(length):  # Przechodzi po wszystkich poprawnych indeksach, od 0 do length - 1.
    ending = ' ' if index < length - 1 else '\n'  # Ustawia spację między wartościami, a po ostatniej koniec wiersza.
    print(arr[index], end=ending)  # Wypisuje bieżący element z odpowiednim zakończeniem.
