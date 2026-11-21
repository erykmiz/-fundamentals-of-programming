# Zadanie 7.10. Zliczamy ujemne liczby parzyste w przedziale domkniętym.


def f(x, y):  # Przyjmuje całkowite granice przedziału.
    count = 0  # Zaczyna zliczanie od zera.
    for number in range(x, y + 1):  # Dodaje 1 do górnej granicy, ponieważ range pomija koniec.
        if number < 0 and number % 2 == 0:  # Wymaga jednocześnie ujemnej wartości i reszty 0 z dzielenia przez 2.
            count += 1  # Zlicza liczbę, gdy oba warunki są spełnione.
    return count  # Zwraca liczbę pasujących wartości.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim włączeniu pliku.
    print(f(-7, 8))  # Pokazuje 3, ponieważ pasują -6, -4 i -2.
    print(f(-1, 11))  # Pokazuje 0, ponieważ jedyna liczba ujemna to nieparzyste -1.
