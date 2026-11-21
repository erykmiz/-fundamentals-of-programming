# Zadanie 7.2. Oddzielamy definicje funkcji od kodu uruchamiającego przykłady.


def add(a, b):  # Definiuje funkcję dodawania z dwoma parametrami.
    return a + b  # Przekazuje sumę do miejsca wywołania funkcji.


def subtract(a, b):  # Definiuje funkcję odejmowania z dwoma parametrami.
    return a - b  # Przekazuje różnicę do miejsca wywołania funkcji.


def main():  # Zbiera przykładowe wywołania w jednej funkcji.
    x = 10  # Ustala pierwszą liczbę do obliczeń.
    y = 5  # Ustala drugą liczbę do obliczeń.
    print(f'Add: {add(x, y)}')  # Wstawia sumę obu liczb do wyświetlanego tekstu.
    print(f'Subtract: {subtract(x, y)}')  # Wstawia różnicę obu liczb do wyświetlanego tekstu.


if __name__ == '__main__':  # Warunek jest prawdziwy przy bezpośrednim uruchomieniu pliku.
    main()  # Uruchamia przykłady. Przy imporcie pliku dostępne będą definicje funkcji.
