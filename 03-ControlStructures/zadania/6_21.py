# Zadanie 6.21: wypłata kwoty najmniejszą liczbą monet 5, 2 i 1 PLN.
amount = int(input('Enter the amount in PLN: '))  # Wczytuje kwotę w pełnych złotych jako liczbę całkowitą.
if amount < 0:  # Odrzuca kwotę ujemną, której nie da się wydać takimi monetami.
    print('The amount cannot be negative.')  # Informuje o błędnej kwocie.
else:  # Oblicza monety dla kwoty nieujemnej.
    coins_5 = amount // 5  # Wybiera maksymalną liczbę monet po 5 PLN.
    remaining = amount % 5  # Oblicza kwotę pozostałą po wydaniu monet po 5 PLN.
    coins_2 = remaining // 2  # Wybiera maksymalną liczbę monet po 2 PLN z pozostałej kwoty.
    coins_1 = remaining % 2  # Pozostałą resztę wydaje monetami po 1 PLN.
    print(f'The amount of PLN {amount} in coins:')  # Wyświetla kwotę, którą rozmieniamy.
    print(f'5 PLN coins: {coins_5}')  # Wyświetla liczbę monet pięciozłotowych.
    print(f'2 PLN coins: {coins_2}')  # Wyświetla liczbę monet dwuzłotowych.
    print(f'1 PLN coins: {coins_1}')  # Wyświetla liczbę monet jednozłotowych.
