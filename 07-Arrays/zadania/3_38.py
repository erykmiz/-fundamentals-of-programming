# Zadanie 3.38. Zamieniamy tablicę dwuwymiarową na jedną listę.

def flatten_array(array):  # Przyjmuje tablicę składającą się z wierszy.
    flattened = []  # Przygotowuje pustą listę na wszystkie elementy.
    for row in array:  # Pobiera kolejne wiersze od góry do dołu.
        for value in row:  # Pobiera kolejne elementy bieżącego wiersza.
            flattened.append(value)  # Dopisuje bieżący element na koniec listy.
    return flattened  # Zwraca listę elementów zachowującą kolejność odczytu.


if __name__ == '__main__':  # Uruchamia przykłady po bezpośrednim otwarciu pliku.
    arrays = [  # Zapisuje trzy podane w poleceniu tablice.
        [[2, 3], [1, 5]],  # Pierwsza tablica ma dwa wiersze po dwie liczby.
        [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]],  # Druga tablica ma dwa wiersze po pięć liczb.
        [[2, 1], [3, 5], [7, 4], [2, 6]],  # Trzecia tablica ma cztery wiersze po dwie liczby.
    ]  # Zamyka listę przykładowych tablic.
    for array in arrays:  # Przechodzi kolejno przez trzy przykłady.
        print(flatten_array(array))  # Wypisuje wynik spłaszczenia jako jedną listę liczb.
