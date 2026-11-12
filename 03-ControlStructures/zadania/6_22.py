# Zadanie 6.22: Wypisujemy liczby 1–30 i sprawdzamy podzielność.
# % daje resztę; reszta 0 oznacza podzielność. Najpierw sprawdzamy wspólne wielokrotności 3 i 5.

for number in range(1, 31):  # Przechodzi przez liczby od 1 do 30 włącznie.
    if number % 3 == 0 and number % 5 == 0:  # Sprawdza podzielność jednocześnie przez 3 i przez 5.
        print('BINGO', end=' ')  # Pokazuje BINGO zamiast liczby i dopisuje spację.
    elif number % 3 == 0:  # Sprawdza podzielność przez 3.
        print('THREE', end=' ')  # Pokazuje THREE zamiast liczby.
    elif number % 5 == 0:  # Sprawdza podzielność przez 5.
        print('FIVE', end=' ')  # Pokazuje FIVE zamiast liczby.
    else:  # Obsługuje liczbę niepodzielną przez 3 ani 5.
        print(number, end=' ')  # Pokazuje samą liczbę i spację zamiast nowej linii.
print()  # Kończy wiersz po całej pętli.
