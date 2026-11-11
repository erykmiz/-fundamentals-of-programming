# Zadanie 6.22: liczby od 1 do 30 i komunikaty o podzielności.
for number in range(1, 31):  # Przechodzi przez liczby od 1 do 30; koniec range nie należy do zakresu.
    if number % 3 == 0 and number % 5 == 0:  # Najpierw sprawdza podzielność przez obie liczby, aby nie wypisać tylko THREE lub FIVE.
        print('BINGO', end=' ')  # Zastępuje wielokrotności 15 słowem BINGO i dodaje spację.
    elif number % 3 == 0:  # Sprawdza podzielność przez 3 dla pozostałych liczb.
        print('THREE', end=' ')  # Zastępuje wielokrotności 3 słowem THREE.
    elif number % 5 == 0:  # Sprawdza podzielność przez 5 dla pozostałych liczb.
        print('FIVE', end=' ')  # Zastępuje wielokrotności 5 słowem FIVE.
    else:  # Obsługuje liczby niepodzielne ani przez 3, ani przez 5.
        print(number, end=' ')  # Wyświetla samą liczbę ze spacją zamiast nowej linii.
print()  # Kończy linię po wyświetleniu wszystkich trzydziestu wyników.
