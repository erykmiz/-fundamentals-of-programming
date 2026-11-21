# Zadanie 1.5. Modyfikujemy pierwszy, ostatni i środkowy element listy.

def print_array(values):  # Przyjmuje listę do wyświetlenia tak jak w przykładzie.
    print('Array:', str(values).replace(', ', ','))  # Zamienia listę na napis i usuwa spacje po przecinkach.


if __name__ == '__main__':  # Uruchamia kolejne zmiany przy bezpośrednim starcie pliku.
    arr = [1, 2, 3, 4, 5]  # Tworzy początkową listę liczb z polecenia.
    print_array(arr)  # Wyświetla listę przed zmianami.
    arr[0] -= 1  # Odejmuje 1 od elementu o indeksie 0, czyli od pierwszego.
    print_array(arr)  # Wyświetla listę po zmianie pierwszej wartości.
    arr[-1] += 4  # Dodaje 4 do ostatniego elementu, który ma indeks -1.
    print_array(arr)  # Wyświetla listę po zmianie ostatniej wartości.
    arr[len(arr) // 2] *= 2  # Wyznacza środkowy indeks i podwaja wartość zapisaną w tym miejscu.
    print_array(arr)  # Wyświetla listę po wszystkich trzech zmianach.
