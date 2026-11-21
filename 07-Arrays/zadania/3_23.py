# Zadanie 3.23. Sprawdzamy, czy wszystkie elementy pierwszej listy występują w drugiej.

def is_subset(first, second):  # Przyjmuje dwie listy do porównania.
    for element in first:  # Sprawdza kolejno elementy pierwszej listy.
        if element not in second:  # Szuka elementu, którego brakuje w drugiej liście.
            return False  # Kończy sprawdzanie po znalezieniu brakującego elementu.
    return True  # Potwierdza, że wszystkie elementy są obecne w drugiej liście.


if __name__ == '__main__':  # Uruchamia przykład przy bezpośrednim otwarciu pliku.
    first = [2, 5, 7]  # Ustawia listę o sprawdzanych elementach.
    second = [5, 1, 2, 7, 9]  # Ustawia listę, w której będziemy szukać.
    print('First array:', first)  # Wypisuje pierwszą listę.
    print('Second array:', second)  # Wypisuje drugą listę.
    print('Is the first array a subset?', is_subset(first, second))  # Wyświetla True, bo wszystkie trzy liczby znaleziono.
