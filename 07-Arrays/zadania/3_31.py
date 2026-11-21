# Zadanie 3.31. Tworzymy tablicę o podanej liczbie wierszy i kolumn wypełnioną zerami.

def create_2d_arr(x, y):  # Przyjmuje liczbę wierszy x i liczbę kolumn y.
    array = []  # Przygotowuje pustą listę na wiersze.
    for _ in range(x):  # Powtarza dodawanie wiersza x razy.
        row = [0] * y  # Tworzy nową listę zawierającą y zer.
        array.append(row)  # Dodaje nowy, niezależny wiersz do tablicy.
    return array  # Zwraca gotową tablicę.


if __name__ == '__main__':  # Uruchamia przykład po bezpośrednim otwarciu tego pliku.
    array = create_2d_arr(3, 5)  # Tworzy trzy wiersze po pięć kolumn.
    for row in array:  # Pobiera każdy wiersz utworzonej tablicy.
        print(*row)  # Wypisuje zera z wiersza, rozdzielając je spacjami.
