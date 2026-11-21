# Zadanie 3.36. Tworzymy i wypisujemy macierze jednostkowe różnych rozmiarów.

def identity_matrix(n):  # Przyjmuje rozmiar kwadratowej macierzy.
    matrix = []  # Przygotowuje pustą listę wierszy macierzy.
    for index in range(n):  # Przechodzi po indeksach wszystkich wierszy.
        row = [0] * n  # Tworzy nowy wiersz zawierający n zer.
        row[index] = 1  # Ustawia jedynkę w miejscu o identycznym indeksie wiersza i kolumny.
        matrix.append(row)  # Dopisuje gotowy wiersz do macierzy.
    return matrix  # Zwraca macierz z jedynkami na głównej przekątnej.


def print_matrix(matrix):  # Przyjmuje tablicę dwuwymiarową do wyświetlenia.
    for row in matrix:  # Pobiera każdy wiersz macierzy.
        print(*row)  # Wypisuje wartości wiersza w osobnych kolumnach.


if __name__ == '__main__':  # Pokazuje przykłady, gdy plik jest uruchomiony bezpośrednio.
    for size in (3, 5, 8):  # Wybiera kolejno trzy rozmiary podane w poleceniu.
        print(f'{size} x {size}')  # Wypisuje wymiary przed każdą macierzą.
        print_matrix(identity_matrix(size))  # Buduje macierz wybranego rozmiaru i ją wyświetla.
