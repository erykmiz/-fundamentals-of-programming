# Zadanie 6.27: Wypisujemy klawiaturę liczbową dwiema pętlami while.
# Pętla z i wybiera wiersz, a pętla z j jego kolumny; j trzeba ustawić od nowa w każdym wierszu.

i = 6  # Ustawia przesunięcie pierwszego wiersza na 6.
while i >= 0:  # Powtarza wiersze dla i równego 6, 3 i 0.
    j = 1  # Zaczyna nowy wiersz od pierwszej kolumny.
    while j <= 3:  # Powtarza trzy kolumny bieżącego wiersza.
        print(f'{i + j}', end=' ')  # Pokazuje cyfrę i spację, np. 6 + 1 daje 7.
        j += 1  # Zwiększa numer kolumny o 1.
    print()  # Kończy wiersz po trzech cyfrach.
    i -= 3  # Zmniejsza przesunięcie o 3, aby przejść do niższego wiersza.
