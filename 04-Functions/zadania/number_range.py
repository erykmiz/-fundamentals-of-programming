# Moduł do zadania 7.5. Sprawdzamy przynależność liczby do przedziału domkniętego.


def in_range(number, x, y):  # Przyjmuje liczbę i obie granice przedziału.
    return x <= number <= y  # Zwraca True, gdy liczba leży w przedziale lub na jego granicy.
