# Zadanie 3.15. Sprawdzamy, czy liczba wpisana z klawiatury występuje w tablicy.

def occurs(number, array):  # Przyjmuje szukaną liczbę i tablicę do sprawdzenia.
    return number in array  # Operator in daje True, gdy przynajmniej jeden element ma tę wartość.


if __name__ == '__main__':  # Uruchamia przykład, gdy plik startuje jako program.
    array = [15, 38, 7, 23, 14]  # Zapisuje liczby, wśród których szukamy.
    number = int(input('Number: '))  # Odczytuje tekst z klawiatury i zamienia go na liczbę całkowitą.
    print('Array:', *array)  # Wyświetla wszystkie elementy tablicy.
    if occurs(number, array):  # Sprawdza, czy liczba występuje w tablicy.
        print(f'Result: number {number} appears in the array')  # Informuje o znalezieniu wartości.
    else:  # Obsługuje wynik False z funkcji occurs.
        print(f'Result: number {number} does not appear in the array')  # Informuje o braku wartości.
