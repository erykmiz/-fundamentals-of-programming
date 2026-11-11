# Zadanie 7.9: sprawdzenie, czy na kostce wypadło 1 lub 6.

import random  # Udostępnia funkcję losującą wynik rzutu kostką.
dice_roll = random.randint(1, 6)  # Losuje liczbę całkowitą od 1 do 6.
special_number = dice_roll == 1 or dice_roll == 6  # Operator or daje True, gdy wynik jest równy 1 lub 6.
print(f'Dice rolled: {dice_roll}')  # Wyświetla wylosowaną liczbę oczek.
print(f'Special number (1 or 6): {special_number}')  # Wyświetla True dla wyniku 1 lub 6, a False dla pozostałych.
