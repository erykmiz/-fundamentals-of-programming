# Zadanie 7.28. Zwracamy liczbę oczek z najdłuższej serii jednakowych rzutów z rzędu.
# Przy remisie wybieramy wcześniejszą serię, a dla pustego zapisu zwracamy None.

def f(dice):  # Przyjmuje tekst, w którym każdy znak oznacza jeden rzut.
    previous = None  # Zapisuje brak poprzedniego wyniku przed pierwszym rzutem.
    current_length = 0  # Przechowuje długość aktualnej serii.
    longest_length = 0  # Przechowuje długość najdłuższej dotychczasowej serii.
    best_roll = None  # Przechowuje liczbę oczek z najdłuższej dotychczasowej serii.
    for roll in dice:  # Odczytuje pojedyncze rzuty od lewej do prawej.
        if roll == previous:  # Sprawdza, czy bieżący rzut przedłuża serię.
            current_length += 1  # Dolicza kolejny taki sam rzut.
        else:  # Rozpoczyna serię dla nowej liczby oczek.
            current_length = 1  # Ustawia długość nowej serii na jeden rzut.
        if current_length > longest_length:  # Porównuje długość bieżącej serii z rekordem.
            longest_length = current_length  # Zapamiętuje nową największą długość.
            best_roll = int(roll)  # Zamienia znak na liczbę oczek i zapamiętuje ją jako wynik.
        previous = roll  # Zachowuje bieżący rzut do porównania w następnym obrocie pętli.
    return best_roll  # Zwraca liczbę oczek z najdłuższej serii.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim otwarciu pliku.
    print(f('5233165554211'))  # Wypisuje 5, bo najdłuższa seria to 555.
    print(f('2133'))  # Wypisuje 3, bo najdłuższa seria to 33.
