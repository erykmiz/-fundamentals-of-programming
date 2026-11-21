# Zadanie 3.20. Wywołujemy funkcje do analizy listy liczb z modułu MyArrays.

import MyArrays  # Wczytuje funkcje zapisane w sąsiednim pliku MyArrays.py.

if __name__ == '__main__':  # Uruchamia przykłady po bezpośrednim otwarciu tego pliku.
    numbers = [7, 3, 8, 5, 2]  # Zapisuje liczby podane w zadaniu.
    print('Numbers:', ','.join(map(str, numbers)))  # Wyświetla dane wejściowe w jednym wierszu.
    print('Second largest number:', MyArrays.second_largest(numbers))  # Pokazuje drugą największą wartość, czyli 7.
    print('Difference between largest and smallest:', MyArrays.range_difference(numbers))  # Pokazuje rozstęp, czyli 6.
    print('Median:', MyArrays.median(numbers))  # Wyświetla medianę, czyli środkową wartość 5.
    smallest, largest = MyArrays.smallest_largest(numbers)  # Rozpakowuje dwuelementową listę z wartościami skrajnymi.
    print(f'Smallest and largest number: {smallest},{largest}')  # Wypisuje minimum i maksimum rozdzielone przecinkiem.
    print('Numbers as a string:', MyArrays.numbers_to_string(numbers))  # Pokazuje listę liczb połączonych myślnikami.
