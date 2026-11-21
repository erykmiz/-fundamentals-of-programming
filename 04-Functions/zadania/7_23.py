# Zadanie 7.23. Sprawdzamy, czy hasło ma co najmniej sześć znaków i czy każdy znak występuje raz.

def f(password):  # Przyjmuje hasło jako napis.
    if len(password) < 6:  # Porównuje liczbę znaków z wymaganą długością.
        return False  # Odrzuca zbyt krótkie hasło.
    for character in password:  # Sprawdza kolejno każdy znak hasła.
        if password.count(character) > 1:  # Szuka znaku występującego więcej niż raz.
            return False  # Odrzuca hasło po znalezieniu powtórzenia.
    return True  # Akceptuje hasło spełniające oba warunki.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim otwarciu pliku.
    print(f('ax15'))  # Wypisuje False dla zbyt krótkiego hasła.
    print(f('book123'))  # Wypisuje False, bo litera o występuje dwa razy.
    print(f('A2water3'))  # Wypisuje True dla poprawnego hasła.
    print(f('qwerty'))  # Wypisuje True dla poprawnego hasła o długości sześciu znaków.
    print(f(''))  # Wypisuje False dla pustego hasła.
