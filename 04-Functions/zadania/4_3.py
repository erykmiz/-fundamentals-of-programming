# Zadanie 4.3. Obliczamy pole trójkąta z długości boków wzorem Herona.

import math  # Udostępnia funkcję sqrt do obliczenia pierwiastka.


def triangle_area(a, b, c):  # Przyjmuje długości trzech boków.
    perimeter = a + b + c  # Sumuje boki, żeby uzyskać obwód trójkąta.
    if min(a, b, c) <= 0 or 2 * max(a, b, c) >= perimeter:  # Sprawdza dodatniość i nierówność trójkąta.
        raise ValueError('The side lengths must form a triangle.')  # Zgłasza błędne długości.
    s = perimeter / 2  # Wyznacza połowę obwodu potrzebną we wzorze Herona.
    return math.sqrt(s * (s - a) * (s - b) * (s - c))  # Zwraca pole obliczone ze wzoru.


if __name__ == '__main__':  # Uruchamia część z klawiaturą i przykładami przy starcie pliku.
    a = float(input('Enter side a: '))  # Wczytuje bok a jako liczbę, także ułamkową.
    b = float(input('Enter side b: '))  # Wczytuje bok b jako liczbę, także ułamkową.
    c = float(input('Enter side c: '))  # Wczytuje bok c jako liczbę, także ułamkową.
    area = triangle_area(a, b, c)  # Oblicza pole dla długości wpisanych przez użytkownika.
    print(f'The area of a triangle with sides {a:g}, {b:g}, {c:g} is {area:g}')  # Pokazuje pole.

    for a, b, c in [(3, 4, 5), (5, 12, 13), (7, 24, 25)]:  # Pobiera kolejne trójki z zadania.
        area = triangle_area(a, b, c)  # Oblicza pole dla bieżącego przykładu.
        print(f'The area of a triangle with sides {a}, {b}, {c} is {area:g}')  # Pokazuje 6, 30 lub 84.
