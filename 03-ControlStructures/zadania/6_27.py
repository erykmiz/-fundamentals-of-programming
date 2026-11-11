# Zadanie 6.27: układ klawiatury liczbowej zapisany dwiema pętlami while.
i = 6  # Zapisuje wartość początkową potrzebną do wyświetlenia górnego wiersza 7, 8, 9.
while i >= 0:  # Wykonuje trzy wiersze dla wartości i równych 6, 3 i 0.
    j = 1  # Zaczyna numerację kolumn od 1 w każdym nowym wierszu.
    while j <= 3:  # Wykonuje trzy kolumny bieżącego wiersza.
        print(f'{i + j}', end=' ')  # Dodaje przesunięcie wiersza do numeru kolumny i wyświetla cyfrę.
        j += 1  # Przechodzi do następnej kolumny, aby pętla wewnętrzna mogła się zakończyć.
    print()  # Przechodzi do nowej linii po trzech cyfrach.
    i -= 3  # Przechodzi do następnego, niższego wiersza klawiatury.
