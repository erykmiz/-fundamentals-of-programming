# Zadanie 3.13. Sortujemy tablice rosnąco metodą bąbelkową.

def bubblesort(array):  # Przyjmuje listę liczb całkowitych do posortowania.
    result = array.copy()  # Tworzy kopię, żeby przemieszczanie liczb nie zmieniało wejściowej listy.
    for end in range(len(result) - 1, 0, -1):  # Po każdym przebiegu skraca obszar sprawdzania o jedną pozycję.
        for index in range(end):  # Odwiedza indeksy lewych elementów sąsiadujących par.
            if result[index] > result[index + 1]:  # Wykrywa parę, w której większa liczba stoi przed mniejszą.
                result[index], result[index + 1] = result[index + 1], result[index]  # Zamienia sąsiednie elementy miejscami.
    return result  # Zwraca posortowaną kopię tablicy.


if __name__ == '__main__':  # Uruchamia przykłady, gdy plik startuje jako program.
    arrays = [[15, 8, 31, 47, 2, 19], [8, -4, 2, -4, 0], [9, 5, 1]]  # Zapisuje trzy przykłady z różnymi układami liczb.
    for array in arrays:  # Przechodzi po przykładowych tablicach.
        print('Array:', *array)  # Wyświetla zawartość przed sortowaniem.
        print('Sorted:', *bubblesort(array))  # Wyświetla wynik sortowania bąbelkowego.
