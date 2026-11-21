# Zadanie 7.24. Obliczamy wartość wyrażenia z pojedynczych cyfr i znaków + lub -.

def f(expression):  # Przyjmuje poprawnie zapisane wyrażenie jako tekst.
    expression = expression.replace(' ', '')  # Usuwa ewentualne spacje między cyframi a operatorami.
    result = int(expression[0])  # Zapisuje wartość pierwszej cyfry jako wynik początkowy.
    for index in range(1, len(expression), 2):  # Odwiedza pozycje operatorów, zaczynając od indeksu 1 i przesuwając się o dwa znaki.
        operator = expression[index]  # Pobiera operator z bieżącej pozycji.
        digit = int(expression[index + 1])  # Zamienia cyfrę tuż za operatorem na liczbę.
        if operator == '+':  # Rozpoznaje dodawanie.
            result += digit  # Zwiększa wynik o wartość cyfry.
        else:  # Pozostały dopuszczalny operator to minus.
            result -= digit  # Zmniejsza wynik o wartość cyfry.
    return result  # Zwraca wynik po wykonaniu działań od lewej do prawej.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim otwarciu pliku.
    print(f('2+3'))  # Wypisuje 5.
    print(f('3+8+1'))  # Wypisuje 12.
    print(f('2+3-4+5-0'))  # Wypisuje 6.
