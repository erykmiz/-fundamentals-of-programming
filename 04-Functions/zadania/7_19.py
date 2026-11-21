# Zadanie 7.19. Sumujemy wszystkie wystąpienia cyfr, które pojawiają się co najmniej dwa razy.

def f(number):  # Przyjmuje liczbę całkowitą.
    digits = str(abs(number))  # Zamienia wartość bezwzględną na napis, żeby można było odczytać cyfry pojedynczo.
    total = 0  # Zaczyna z sumą równą zero.
    for digit in digits:  # Przechodzi po każdym wystąpieniu cyfry.
        if digits.count(digit) > 1:  # Liczy wystąpienia tej cyfry i sprawdza, czy jest ich więcej niż jedno.
            total += int(digit)  # Zamienia bieżący znak na liczbę i dolicza ją do wyniku.
    return total  # Zwraca sumę cyfr, które się powtarzają.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim otwarciu pliku.
    print(f(1027))  # Wypisuje 0, bo żadna cyfra się nie powtarza.
    print(f(230335))  # Wypisuje 9 jako sumę trzech trójek.
    print(f(513553007))  # Wypisuje 21 jako sumę trzech piątek, dwóch trójek i dwóch zer.
