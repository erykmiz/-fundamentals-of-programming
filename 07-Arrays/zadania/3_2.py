# Zadanie 3.2. Tworzymy i wypisujemy wszystkie czternaście tablic z polecenia.

import random  # Udostępnia funkcję randint do losowania liczb całkowitych.

arr1 = [3, 7, 1, 0, 4]  # Tworzy listę z pięciu podanych liczb.
arr2 = [[2, 3], [7, 1], [0, 4]]  # Tworzy tablicę z trzech dwuelementowych wierszy.
arr3 = [7 for _ in range(5)]  # Wpisuje liczbę 7 pięć razy. Podkreślenie zastępuje nieużywany licznik.
arr4 = [i for i in range(1, 10)]  # Zbiera liczby od 1 do 9, bo range pomija górną granicę.
arr5 = [i * 2 for i in range(1, 10)]  # Podwaja każdą liczbę od 1 do 9.
arr6 = [random.randint(1, 20) for _ in range(10)]  # Losuje dziesięć liczb od 1 do 20 włącznie.
arr7 = [[] for _ in range(5)]  # Tworzy pięć osobnych pustych list.
arr8 = [[1 for _ in range(2)] for _ in range(4)]  # Tworzy cztery wiersze po dwie jedynki.
arr9 = [[random.randint(1, 20) for _ in range(3)] for _ in range(5)]  # Losuje po trzy liczby w każdym z pięciu wierszy.
arr10 = [4, 0, 3]  # Zapisuje trzy wartości w podanej kolejności.
arr11 = [0] * 15  # Powtarza element 0 piętnaście razy.
arr12 = list(range(1, 31))  # Tworzy listę wszystkich liczb całkowitych od 1 do 30.
arr13 = [random.randint(0, 1) for _ in range(20)]  # Losuje dwadzieścia zer lub jedynek.
arr14 = [[False for _ in range(2)] for _ in range(5)]  # Tworzy pięć osobnych wierszy po dwie wartości False.

arrays = [arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9, arr10, arr11, arr12, arr13, arr14]  # Zbiera tablice w kolejności z polecenia.
for index, array in enumerate(arrays, start=1):  # Pobiera tablice z kolejnymi numerami od 1.
    print(f'arr{index}:', array)  # Wyświetla nazwę przykładowej tablicy i jej zawartość.
