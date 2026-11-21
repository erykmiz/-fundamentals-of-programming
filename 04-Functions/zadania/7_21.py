# Zadanie 7.21. Obliczamy różnicę między największą a najmniejszą z trzech liczb.

def f(number1, number2, number3):  # Przyjmuje trzy liczby do porównania.
    largest = max(number1, number2, number3)  # Wybiera największą z trzech wartości.
    smallest = min(number1, number2, number3)  # Wybiera najmniejszą z trzech wartości.
    return largest - smallest  # Zwraca różnicę pomiędzy znalezionymi wartościami.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim otwarciu pliku.
    print(f(7, 4, 9))  # Wypisuje 5, czyli 9 minus 4.
    print(f(2, 12, 8))  # Wypisuje 10, czyli 12 minus 2.
