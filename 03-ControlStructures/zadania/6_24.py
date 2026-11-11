# Zadanie 6.24: wzór z gwiazdek, najpierw rosnący, a potem malejący.
for count in range(1, 6):  # Ustawia liczbę gwiazdek w rosnących wierszach od 1 do 5.
    print(('* ' * count).rstrip())  # Powtarza tekst gwiazdki ze spacją i usuwa ostatnią zbędną spację.
for count in range(4, 0, -1):  # Ustawia liczbę gwiazdek w malejących wierszach na 4, 3, 2 i 1.
    print(('* ' * count).rstrip())  # Wyświetla malejącą liczbę gwiazdek w osobnych wierszach.
