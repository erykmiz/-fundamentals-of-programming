# Zadanie 7.12. Budujemy napis z gwiazdek rozdzielonych ukośnikami.


def f(n):  # Przyjmuje liczbę gwiazdek.
    stars = '*' * n  # Tworzy napis zawierający n gwiazdek.
    return '/'.join(stars)  # Wstawia ukośnik pomiędzy sąsiednie znaki napisu.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim włączeniu pliku.
    print(f(4))  # Pokazuje cztery gwiazdki rozdzielone trzema ukośnikami.
    print(f(1))  # Pokazuje jedną gwiazdkę bez ukośników.
