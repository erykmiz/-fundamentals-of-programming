# Zadanie 7.14. Wybieramy działanie arytmetyczne na podstawie podanego operatora.


def f(number1, number2, operator):  # Przyjmuje dwie liczby oraz znak działania zapisany jako tekst.
    if operator == '+':  # Rozpoznaje dodawanie.
        return number1 + number2  # Zwraca sumę obu liczb.
    if operator == '-':  # Rozpoznaje odejmowanie.
        return number1 - number2  # Odejmuje drugą liczbę od pierwszej.
    if operator == '*':  # Rozpoznaje mnożenie.
        return number1 * number2  # Zwraca iloczyn obu liczb.
    if operator == '%':  # Rozpoznaje dzielenie z resztą.
        return number1 % number2  # Zwraca resztę z dzielenia pierwszej liczby przez drugą.
    if operator == '**':  # Rozpoznaje potęgowanie.
        return number1 ** number2  # Podnosi pierwszą liczbę do potęgi określonej przez drugą.
    raise ValueError('Unknown operator')  # Zgłasza błąd, gdy żadne działanie nie pasuje.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim włączeniu pliku.
    print(f(2, 3, '+'))  # Pokazuje sumę 5.
    print(f(2, 3, '%'))  # Pokazuje resztę 2.
    print(f(2, 3, '**'))  # Pokazuje potęgę 8.
    print(f(2, 3, '*'))  # Pokazuje iloczyn 6.
    print(f(2, 3, '-'))  # Pokazuje różnicę -1.
