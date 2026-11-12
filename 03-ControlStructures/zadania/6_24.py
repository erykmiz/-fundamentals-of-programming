# Zadanie 6.24: Rysujemy rosnące i malejące rzędy gwiazdek.
# Tekst * liczba powtarza tekst; rstrip() usuwa spację na końcu wiersza.
# range(4, 0, -1) daje 4, 3, 2, 1: krok -1 zmniejsza wartość, a końcowe 0 nie wchodzi.

for count in range(1, 6):  # Wybiera liczby gwiazdek od 1 do 5.
    print(('* ' * count).rstrip())  # Pokazuje wybraną liczbę gwiazdek bez końcowej spacji.
for count in range(4, 0, -1):  # Wybiera liczby gwiazdek od 4 do 1.
    print(('* ' * count).rstrip())  # Pokazuje kolejne malejące wiersze.
