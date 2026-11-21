# Zadanie 7.20. Szukamy n-tej liczby pierwszej, zaczynając od 2.

def is_prime(number):  # Sprawdza, czy podana liczba całkowita jest pierwsza.
    if number < 2:  # Odrzuca liczby mniejsze od najmniejszej liczby pierwszej.
        return False  # Zwraca False dla liczb ujemnych, zera i jedynki.
    divisor = 2  # Zaczyna sprawdzanie od najmniejszego możliwego dzielnika poza jedynką.
    while divisor * divisor <= number:  # Wystarczy dojść do pierwiastka, bo większy dzielnik miałby mniejszą parę.
        if number % divisor == 0:  # Reszta zero oznacza, że liczba dzieli się przez bieżący dzielnik.
            return False  # Kończy sprawdzanie, bo znaleziono dzielnik.
        divisor += 1  # Przechodzi do następnego możliwego dzielnika.
    return True  # Zwraca True po sprawdzeniu wszystkich potrzebnych dzielników.


def f(n):  # Przyjmuje numer szukanej liczby pierwszej, licząc od 1.
    if n < 1:  # Sprawdza, czy podana pozycja należy do ciągu.
        raise ValueError('n musi być większe od zera.')  # Zgłasza błąd dla zera lub liczby ujemnej.
    candidate = 1  # Ustawia wartość początkową tak, aby najpierw sprawdzić liczbę 2.
    found = 0  # Przechowuje liczbę dotąd znalezionych liczb pierwszych.
    while found < n:  # Szuka, dopóki licznik nie osiągnie podanej pozycji.
        candidate += 1  # Przechodzi do kolejnej liczby do sprawdzenia.
        if is_prime(candidate):  # Wywołuje funkcję sprawdzającą bieżącą liczbę.
            found += 1  # Zwiększa licznik po znalezieniu liczby pierwszej.
    return candidate  # Zwraca ostatnią znalezioną liczbę pierwszą.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim otwarciu pliku.
    print(f(1))  # Wypisuje 2, czyli pierwszą liczbę pierwszą.
    print(f(5))  # Wypisuje 11, czyli piątą liczbę pierwszą.
