# Zadanie 6.23: Tworzymy tabliczkę mnożenia przez liczby 1–10.
# range(1, 11) pomija końcowe 11; f wstawia wartości i obliczenia z {} do tekstu.

number = int(input('Enter number: '))  # Pobiera liczbę do mnożenia i zamienia ją na int.
for multiplier in range(1, 11):  # Wybiera mnożniki kolejno od 1 do 10.
    print(f'{number} x {multiplier} = {number * multiplier}')  # Pokazuje działanie i jego wynik, np. 6 x 2 = 12.
