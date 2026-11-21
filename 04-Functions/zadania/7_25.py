# Zadanie 7.25. Sumujemy liczby podzielne przez 2 i 3, których nie da się podzielić przez 4 bez reszty.

def f(x, y):  # Przyjmuje początek i koniec przedziału włącznie.
    total = 0  # Zaczyna od sumy równej zero.
    for number in range(x, y + 1):  # Przechodzi po liczbach od x do y, bo range pomija swój koniec.
        if number % 2 == 0 and number % 3 == 0 and number % 4 != 0:  # Sprawdza trzy warunki za pomocą reszty z dzielenia.
            total += number  # Dodaje bieżącą liczbę, gdy wszystkie warunki są spełnione.
    return total  # Zwraca sumę zakwalifikowanych liczb.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim otwarciu pliku.
    print(f(1, 20))  # Wypisuje 24 jako sumę 6 i 18.
    print(f(10, 30))  # Wypisuje 48 jako sumę 18 i 30.
