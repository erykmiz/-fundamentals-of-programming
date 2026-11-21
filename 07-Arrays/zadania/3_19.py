# Zadanie 3.19. Zliczamy wystąpienia wskazanej wartości w krotce.

def count_occurrences(values, value):  # Przyjmuje krotkę i wartość, której szukamy.
    return values.count(value)  # Zwraca liczbę elementów równych podanej wartości.


if __name__ == '__main__':  # Pokazuje przykład przy bezpośrednim uruchomieniu pliku.
    numbers = (50, 20, 40, 50, 30, 50)  # Tworzy krotkę z kilkoma powtórzeniami liczby 50.
    value = 50  # Wskazuje liczbę do zliczenia.
    count = count_occurrences(numbers, value)  # Wywołuje funkcję i zapisuje liczbę wystąpień.
    print('Tuple:', ','.join(map(str, numbers)))  # Wypisuje wszystkie liczby rozdzielone przecinkami.
    print('Value:', value)  # Wypisuje wartość, którą zliczamy.
    print('Number of occurrences:', count)  # Pokazuje wynik, czyli 3.
