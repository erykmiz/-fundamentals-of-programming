# Zadanie 6.3: tworzymy skrót KUE z nazwy Krakow University of Economics.
# Indeksy liczymy od 0; spacje także zajmują pozycje w tekście.

university = "Krakow University of Economics"  # Zapamiętuje pełną nazwę uczelni, razem ze spacjami.

abbreviation = university[0] + university[7] + university[21]  # Pobiera K, U i E i zapisuje połączony tekst KUE.
print(abbreviation)  # print() pokazuje zawartość zmiennej abbreviation, czyli KUE.
