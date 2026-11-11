# Zadanie 7.10: odgadnięcie wyniku rzutu kostką wykonanego przez komputer.

import random  # Udostępnia funkcję do losowania wyniku rzutu kostką.
computer = random.randint(1, 6)  # Losuje wynik komputera, nie pokazując go przed odgadnięciem.
you = int(input('Guess the dice number (1-6): '))  # Wczytuje Twój typ i zamienia tekst na liczbę całkowitą.
you_won = you == computer  # Porównuje obie liczby; dwa znaki == oznaczają sprawdzenie równości.
print(f'You won: {you_won}')  # Wyświetla True, jeśli odgadnięto wynik, albo False, jeśli typ był inny.
