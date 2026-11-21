# Zadanie 7.27. Sprawdzamy, czy ostatnia cyfra kodu jest poprawną cyfrą kontrolną.

def f(product_code):  # Przyjmuje kod jako napis, żeby zachować ewentualne zero na początku.
    if len(product_code) != 4:  # Sprawdza, czy kod zawiera dokładnie cztery znaki.
        return False  # Odrzuca kod o innej długości.
    total = 0  # Zaczyna od sumy pierwszych trzech cyfr równej zero.
    for digit in product_code:  # Sprawdza każdy znak, łącznie z cyfrą kontrolną.
        if digit not in '0123456789':  # Szuka znaku spoza zestawu cyfr dziesiętnych.
            return False  # Kończy sprawdzanie przy znaku, który nie jest cyfrą kodu.
    for digit in product_code[:3]:  # Wybiera trzy pierwsze cyfry kodu.
        total += int(digit)  # Zamienia bieżącą cyfrę na liczbę i dodaje ją do sumy.
    return total % 7 == int(product_code[3])  # Porównuje resztę z dzielenia sumy przez 7 z czwartą cyfrą.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim otwarciu pliku.
    print(f('1082'))  # Wypisuje True, bo 9 daje resztę 2.
    print(f('2035'))  # Wypisuje True, bo 5 daje resztę 5.
    print(f('1114'))  # Wypisuje False, bo poprawna cyfra kontrolna to 3.
    print(f('7071'))  # Wypisuje False, bo poprawna cyfra kontrolna to 0.
