# Zadanie 7.15. Sprawdzamy, czy co najmniej trzy osoby były jednocześnie w pokoju.


def f(detector):  # Przyjmuje zapis wejść „+” i wyjść „-” jako napis.
    people = 0  # Na początku pokój jest pusty.
    for event in detector:  # Czyta zdarzenia w kolejności, w której zarejestrował je czujnik.
        if event == '+':  # Odczytuje plus jako wejście jednej osoby.
            people += 1  # Zwiększa bieżącą liczbę osób o 1.
        elif event == '-':  # Odczytuje minus jako wyjście jednej osoby.
            people -= 1  # Zmniejsza bieżącą liczbę osób o 1.
        if people >= 3:  # Sprawdza liczbę osób po danym zdarzeniu.
            return True  # Kończy funkcję, gdy próg został osiągnięty chociaż raz.
    return False  # Zwraca False, gdy próg nie został osiągnięty.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim włączeniu pliku.
    print(f('+-+++-+---'))  # Pokazuje True, bo po trzech kolejnych wejściach w pokoju są trzy osoby.
    print(f('+-+-+-+-'))  # Pokazuje False, bo wejścia i wyjścia występują na zmianę.
    print(f('+-++-+--'))  # Pokazuje False, bo w pokoju są najwyżej dwie osoby.
    print(f('+-++-++-+---'))  # Pokazuje True, bo licznik osiąga 3.
