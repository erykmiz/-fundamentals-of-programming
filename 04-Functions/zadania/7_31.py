# Zadanie 7.31. Rekurencyjnie podnosimy liczbę do potęgi o wykładniku całkowitym.

def power(x, n):  # Przyjmuje podstawę x oraz wykładnik n.
    if n == 0:  # Rozpoznaje przypadek bazowy, który zatrzymuje rekurencję.
        return 1  # Zwraca 1 dla potęgi o wykładniku zero.
    if n < 0:  # Rozpoznaje wykładnik ujemny.
        return 1 / power(x, -n)  # Oblicza odwrotność potęgi o dodatnim wykładniku.
    return x * power(x, n - 1)  # Mnoży podstawę przez potęgę o wykładniku o jeden mniejszym.


if __name__ == '__main__':  # Uruchamia przykład przy bezpośrednim otwarciu pliku.
    print(power(5, 3))  # Wypisuje 125, czyli 5 do potęgi trzeciej.
