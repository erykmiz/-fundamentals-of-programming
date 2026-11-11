# Zadanie 6.30: kupon liczb od 1 do 49 w siedmiu wierszach i kolumnach.
for row in range(1, 8):  # Ustawia pierwszą liczbę wiersza kolejno na 1, 2, aż do 7.
    for number in range(row, 50, 7):  # Wybiera liczby danego wiersza, zwiększając każdą następną o 7.
        print(number, end=' ')  # Wyświetla jedną liczbę i spację bez kończenia wiersza.
    print()  # Przechodzi do nowego wiersza po wypisaniu jego siedmiu liczb.
