# Zadanie 7.11. Sprawdzamy, czy co najmniej jedna z trzech liczb jest ujemna.


def f(n1, n2, n3):  # Przyjmuje trzy liczby do porównania z zerem.
    return n1 < 0 or n2 < 0 or n3 < 0  # Operator or daje True, gdy chociaż jedno porównanie jest prawdziwe.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim włączeniu pliku.
    print(f(11, 6, -4))  # Pokazuje True, bo -4 jest ujemne.
    print(f(5, 4, 14))  # Pokazuje False, bo wszystkie trzy liczby są dodatnie.
