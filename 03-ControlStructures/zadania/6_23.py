# Zadanie 6.23: tabliczka mnożenia podanej liczby przez liczby od 1 do 10.
number = int(input('Enter number: '))  # Wczytuje liczbę, dla której powstanie tabliczka mnożenia.
for multiplier in range(1, 11):  # Ustawia mnożnik kolejno na 1, 2, aż do 10.
    print(f'{number} x {multiplier} = {number * multiplier}')  # Wyświetla jedno działanie oraz jego wynik.
