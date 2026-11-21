# Zadanie 4.2. Definiujemy funkcję dodającą dwie liczby i wywołujemy ją na przykładzie.

def add(a, b):  # def tworzy funkcję add, która przyjmuje dwa parametry.
    result = a + b  # Dodaje wartości przekazane w a i b.
    return result  # Zwraca obliczoną sumę w miejsce wywołania funkcji.


if __name__ == '__main__':  # Wykonuje przykład przy bezpośrednim uruchomieniu pliku.
    sum_value = add(5, 3)  # Przekazuje 5 jako a i 3 jako b oraz zapisuje wynik.
    print(sum_value)  # Wyświetla wynik dodawania, czyli 8.
