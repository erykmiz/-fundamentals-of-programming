# Zadanie 7.7. Sprawdzamy, czy napis jest poprawną liczbą binarną.


def f(binary_number):  # Przyjmuje zapis liczby jako tekst.
    if binary_number == '':  # Sprawdza, czy wpisano pusty tekst.
        return False  # Odrzuca zapis bez żadnej cyfry.
    for digit in binary_number:  # Przegląda znaki od lewej do prawej.
        if digit not in '01':  # Sprawdza, czy znak wykracza poza dwie dozwolone cyfry.
            return False  # Kończy sprawdzanie po znalezieniu błędnego znaku.
    return True  # Potwierdza, że wszystkie znaki to 0 lub 1.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim włączeniu pliku.
    print(f('101101'))  # Pokazuje True dla poprawnej liczby binarnej.
    print(f('1311a10100'))  # Pokazuje False dla napisu zawierającego inne znaki.
