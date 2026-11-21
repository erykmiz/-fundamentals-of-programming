# Zadanie 7.8. Liczymy najmniejszą liczbę monet do zapłaty w automacie.


def f(amount_to_pay):  # Przyjmuje kwotę w pełnych złotych.
    coins_5 = amount_to_pay // 5  # Bierze tyle monet 5 zł, ile mieści się w kwocie.
    remainder = amount_to_pay % 5  # Oblicza kwotę pozostałą po użyciu monet 5 zł.
    coins_2 = remainder // 2  # Bierze tyle monet 2 zł, ile mieści się w reszcie.
    coins_1 = remainder % 2  # Zamienia ostatnią resztę, równą 0 lub 1 zł, na liczbę monet 1 zł.
    return coins_5 + coins_2 + coins_1  # Zwraca łączną liczbę monet trzech nominałów.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim włączeniu pliku.
    print(f(23))  # Pokazuje 6 monet: cztery 5 zł, jedną 2 zł i jedną 1 zł.
    print(f(8))  # Pokazuje 3 monety: 5 zł, 2 zł i 1 zł.
    print(f(2))  # Pokazuje 1 monetę o nominale 2 zł.
    print(f(0))  # Pokazuje 0 monet, gdy kwota wynosi 0 zł.
