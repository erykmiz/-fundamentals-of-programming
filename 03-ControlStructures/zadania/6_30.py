# Zadanie 6.30: Wypisujemy kupon 7 × 7 z liczbami od 1 do 49.
# Zewnętrzna pętla wybiera wiersz, a wewnętrzna jego liczby; krok 7 daje np. 1, 8, 15.

for row in range(1, 8):  # Wybiera pierwsze liczby wierszy: 1, 2, aż do 7.
    for number in range(row, 50, 7):  # Wybiera liczby wiersza co 7, nie przekraczając 49.
        print(number, end=' ')  # Pokazuje liczbę i spację zamiast nowej linii.
    print()  # Kończy wiersz po siedmiu liczbach.
