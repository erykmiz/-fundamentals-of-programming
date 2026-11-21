# Zadanie 4.7. Literujemy imię za pomocą słów alfabetu fonetycznego ICAO.
# Alfabet obejmuje litery od A do Z. Dla pozostałych znaków funkcja zwraca ???.

def icao(letter):  # Przyjmuje znak i wybiera odpowiadające mu słowo.
    letter = letter.capitalize()  # Zamienia pojedynczą małą literę na wielką.
    if letter == 'A':  # Sprawdza, czy przekazano literę A.
        icao_name = 'Alfa'  # Przypisuje słowo kodowe dla A.
    elif letter == 'B':  # Sprawdza następną możliwość, czyli literę B.
        icao_name = 'Bravo'  # Przypisuje słowo kodowe dla B.
    elif letter == 'C':  # Sprawdza, czy przekazano literę C.
        icao_name = 'Charlie'  # Przypisuje słowo kodowe dla C.
    elif letter == 'D':  # Sprawdza, czy przekazano literę D.
        icao_name = 'Delta'  # Przypisuje słowo kodowe dla D.
    elif letter == 'E':  # Sprawdza, czy przekazano literę E.
        icao_name = 'Echo'  # Przypisuje słowo kodowe dla E.
    elif letter == 'F':  # Sprawdza, czy przekazano literę F.
        icao_name = 'Foxtrot'  # Przypisuje słowo kodowe dla F.
    elif letter == 'G':  # Sprawdza, czy przekazano literę G.
        icao_name = 'Golf'  # Przypisuje słowo kodowe dla G.
    elif letter == 'H':  # Sprawdza, czy przekazano literę H.
        icao_name = 'Hotel'  # Przypisuje słowo kodowe dla H.
    elif letter == 'I':  # Sprawdza, czy przekazano literę I.
        icao_name = 'India'  # Przypisuje słowo kodowe dla I.
    elif letter == 'J':  # Sprawdza, czy przekazano literę J.
        icao_name = 'Juliett'  # Przypisuje słowo kodowe dla J.
    elif letter == 'K':  # Sprawdza, czy przekazano literę K.
        icao_name = 'Kilo'  # Przypisuje słowo kodowe dla K.
    elif letter == 'L':  # Sprawdza, czy przekazano literę L.
        icao_name = 'Lima'  # Przypisuje słowo kodowe dla L.
    elif letter == 'M':  # Sprawdza, czy przekazano literę M.
        icao_name = 'Mike'  # Przypisuje słowo kodowe dla M.
    elif letter == 'N':  # Sprawdza, czy przekazano literę N.
        icao_name = 'November'  # Przypisuje słowo kodowe dla N.
    elif letter == 'O':  # Sprawdza, czy przekazano literę O.
        icao_name = 'Oscar'  # Przypisuje słowo kodowe dla O.
    elif letter == 'P':  # Sprawdza, czy przekazano literę P.
        icao_name = 'Papa'  # Przypisuje słowo kodowe dla P.
    elif letter == 'Q':  # Sprawdza, czy przekazano literę Q.
        icao_name = 'Quebec'  # Przypisuje słowo kodowe dla Q.
    elif letter == 'R':  # Sprawdza, czy przekazano literę R.
        icao_name = 'Romeo'  # Przypisuje słowo kodowe dla R.
    elif letter == 'S':  # Sprawdza, czy przekazano literę S.
        icao_name = 'Sierra'  # Przypisuje słowo kodowe dla S.
    elif letter == 'T':  # Sprawdza, czy przekazano literę T.
        icao_name = 'Tango'  # Przypisuje słowo kodowe dla T.
    elif letter == 'U':  # Sprawdza, czy przekazano literę U.
        icao_name = 'Uniform'  # Przypisuje słowo kodowe dla U.
    elif letter == 'V':  # Sprawdza, czy przekazano literę V.
        icao_name = 'Victor'  # Przypisuje słowo kodowe dla V.
    elif letter == 'W':  # Sprawdza, czy przekazano literę W.
        icao_name = 'Whiskey'  # Przypisuje słowo kodowe dla W.
    elif letter == 'X':  # Sprawdza, czy przekazano literę X.
        icao_name = 'X-ray'  # Przypisuje słowo kodowe dla X.
    elif letter == 'Y':  # Sprawdza, czy przekazano literę Y.
        icao_name = 'Yankee'  # Przypisuje słowo kodowe dla Y.
    elif letter == 'Z':  # Sprawdza, czy przekazano literę Z.
        icao_name = 'Zulu'  # Przypisuje słowo kodowe dla Z.
    else:  # Obsługuje znak spoza liter przewidzianych przez funkcję.
        icao_name = '???'  # Przypisuje zastępczy tekst dla nieznanego znaku.

    return icao_name  # Zwraca wybrane słowo do miejsca wywołania funkcji.


if __name__ == '__main__':  # Wczytuje imię i literuje je przy bezpośrednim uruchomieniu programu.
    name = input('Enter your name: ')  # Pobiera imię wpisane na klawiaturze.
    print('ICAO words for spelling out your name:')  # Wyświetla nagłówek wyniku.
    for char in name:  # Pobiera kolejne znaki wczytanego imienia.
        word = icao(char)  # Zamienia bieżący znak na słowo alfabetu ICAO.
        print(word, end=' ')  # Wyświetla słowo i spację, zostając w tym samym wierszu.
    print()  # Przechodzi do nowego wiersza po wypisaniu całego imienia.
