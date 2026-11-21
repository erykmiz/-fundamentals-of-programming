# Zadanie 3.11. Porównujemy długości tablic oraz wartości na tych samych pozycjach.

def compare(array1, array2):  # Przyjmuje dwie tablice do porównania.
    if len(array1) != len(array2):  # Sprawdza, czy tablice mają różne długości.
        return False  # Kończy porównanie, gdy liczba elementów się różni.
    for index in range(len(array1)):  # Przechodzi przez wszystkie wspólne indeksy.
        if array1[index] != array2[index]:  # Sprawdza, czy wartości pod tym samym indeksem się różnią.
            return False  # Kończy porównanie po znalezieniu pierwszej różnicy.
    return True  # Zwraca prawdę, gdy wszystkie odpowiadające sobie elementy są równe.


if __name__ == '__main__':  # Uruchamia przykłady, gdy plik startuje jako program.
    pairs = [  # Zbiera cztery pary tablic do sprawdzenia.
        (['water', 'book', 'sky'], ['water', 'book', 'sky']),  # Para identycznych tablic napisów.
        ([True, False], [True, False, True]),  # Para tablic logicznych o różnych długościach.
        ([5, 3, 1], [5, 3, 1]),  # Para identycznych tablic liczb.
        ([3, 2, 1], [3, 2]),  # Para tablic liczb o różnych długościach.
    ]  # Zamyka listę przykładowych par.

    for array1, array2 in pairs:  # Rozpakowuje kolejne pary do dwóch zmiennych.
        print('Array1:', *array1)  # Wypisuje elementy pierwszej tablicy.
        print('Array2:', *array2)  # Wypisuje elementy drugiej tablicy.
        if compare(array1, array2):  # Sprawdza wynik porównania obu tablic.
            print('Comparison: arrays are the same')  # Informuje o zgodności tablic.
        else:  # Obsługuje przypadek, w którym porównanie dało False.
            print('Comparison: arrays are different')  # Informuje o różnicy tablic.
        print()  # Oddziela ten wynik od kolejnej pary pustym wierszem.
