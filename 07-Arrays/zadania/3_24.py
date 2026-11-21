# Zadanie 3.24. Losujemy i wyświetlamy kilka elementów z listy.

import random  # Udostępnia moduł z funkcjami losującymi.


def rand_elem(array):  # Przyjmuje niepustą listę, z której losujemy.
    return random.choice(array)  # Zwraca jeden losowo wybrany element listy.


if __name__ == '__main__':  # Wykonuje losowania przy bezpośrednim uruchomieniu pliku.
    numbers = [12, 28, 36, 44, 51]  # Przygotowuje przykładowe elementy do losowania.
    for _ in range(5):  # Powtarza losowanie pięć razy. Znak _ zastępuje nieużywany licznik.
        print(rand_elem(numbers))  # Wyświetla element, który może się powtórzyć przy kolejnym losowaniu.
