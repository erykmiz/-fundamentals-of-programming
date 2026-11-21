# Zadanie 7.17. Sprawdzamy, czy podany tekst czyta się tak samo od końca.
# Porównujemy znaki dokładnie tak, jak je podano, łącznie z myślnikami i wielkością liter.

def f(palindrome):  # Przyjmuje tekst do sprawdzenia.
    reversed_text = palindrome[::-1]  # Buduje kopię napisu, przechodząc po znakach od końca.
    return palindrome == reversed_text  # Zwraca True, gdy oryginał i odwrócony napis są identyczne.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim otwarciu pliku.
    print(f('radar'))  # Wypisuje True dla słowa radar.
    print(f('12-11-21'))  # Wypisuje True dla tekstu zawierającego myślniki.
    print(f('book'))  # Wypisuje False, bo odwrócony napis to koob.
