# Zadanie 7.13. Łączymy liczby od 1 do n w jeden napis.


def f(n):  # Przyjmuje ostatnią liczbę, która ma trafić do napisu.
    result = ''  # Zaczyna od pustego tekstu.
    for number in range(1, n + 1):  # Przechodzi od 1 do n włącznie.
        result += str(number)  # Zamienia liczbę na tekst i dopisuje ją na końcu.
    return result  # Zwraca napis zawierający wszystkie kolejne liczby.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim włączeniu pliku.
    print(f(11))  # Pokazuje liczby od 1 do 11 połączone bez odstępów.
    print(f(4))  # Pokazuje napis „1234”.
