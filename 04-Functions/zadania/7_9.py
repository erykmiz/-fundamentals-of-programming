# Zadanie 7.9. Sumujemy cyfry parzyste lub nieparzyste według parametru even.


def f(number, even):  # Przyjmuje liczbę oraz True dla cyfr parzystych lub False dla nieparzystych.
    total = 0  # Zaczyna sumowanie od zera.
    for character in str(abs(number)):  # Zamienia wartość bezwzględną na tekst i przegląda cyfry.
        digit = int(character)  # Zamienia tekstowy znak cyfry na liczbę.
        is_even = digit % 2 == 0  # Sprawdza, czy dzielenie cyfry przez 2 daje resztę 0.
        if is_even == even:  # Wybiera cyfrę o parzystości wskazanej przez parametr even.
            total += digit  # Dodaje wartość wybranej cyfry do sumy.
    return total  # Zwraca sumę po przejrzeniu wszystkich cyfr.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim włączeniu pliku.
    print(f(3124, True))  # Pokazuje sumę cyfr 2 i 4, czyli 6.
    print(f(3124, False))  # Pokazuje sumę cyfr 3 i 1, czyli 4.
    print(f(20576, False))  # Pokazuje sumę cyfr 5 i 7, czyli 12.
    print(f(20576, True))  # Pokazuje sumę cyfr 2, 0 i 6, czyli 8.
    print(f(13115, True))  # Pokazuje 0, ponieważ wszystkie cyfry są nieparzyste.
