# Zadanie 7.29. Liczymy silnię rekurencyjnie.
# Dla 5 wywołania schodzą do 1, a przy powrocie mnożą wartości 5, 4, 3, 2 i 1.

def factorial(n):  # Przyjmuje nieujemną liczbę całkowitą n.
    if n < 0:  # Sprawdza, czy argument nie jest ujemny.
        raise ValueError('Silnia wymaga liczby nieujemnej.')  # Zgłasza błąd dla wartości spoza zakresu.
    if n == 0 or n == 1:  # Rozpoznaje przypadki bazowe, które zatrzymują rekurencję.
        return 1  # Zarówno 0!, jak i 1! mają wartość 1.
    return n * factorial(n - 1)  # Mnoży n przez silnię liczby o jeden mniejszej.


if __name__ == '__main__':  # Uruchamia przykład przy bezpośrednim otwarciu pliku.
    print(factorial(5))  # Wypisuje 120, czyli wartość 5!.
