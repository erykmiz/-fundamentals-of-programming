# Zadanie 7.30. Rekurencyjnie sumujemy liczby naturalne od 1 do n.

def sum_natural(n):  # Przyjmuje górną granicę przedziału.
    if n < 0:  # Sprawdza, czy podana granica jest ujemna.
        raise ValueError('n musi być nieujemne.')  # Zgłasza błąd dla ujemnej granicy.
    if n == 0:  # Zatrzymuje rekurencję po wyczerpaniu liczb do dodania.
        return 0  # Suma pustego przedziału wynosi zero.
    return n + sum_natural(n - 1)  # Dodaje n do sumy liczb od 1 do n - 1.


if __name__ == '__main__':  # Uruchamia przykład przy bezpośrednim otwarciu pliku.
    print(sum_natural(10))  # Wypisuje 55, czyli sumę liczb od 1 do 10.
