# Zadanie 7.8: trzy rzuty kostką i suma uzyskanych oczek.

import random  # Udostępnia funkcję randint() do losowania liczby oczek na kostce.
dice_roll_1 = random.randint(1, 6)  # Losuje wynik pierwszego rzutu: liczbę od 1 do 6.
dice_roll_2 = random.randint(1, 6)  # Losuje wynik drugiego rzutu niezależnie od pierwszego.
dice_roll_3 = random.randint(1, 6)  # Losuje wynik trzeciego rzutu.
total = dice_roll_1 + dice_roll_2 + dice_roll_3  # Dodaje liczbę oczek ze wszystkich trzech rzutów.
print(f'Dice rolls: {dice_roll_1}, {dice_roll_2}, {dice_roll_3}')  # Wyświetla osobno wynik każdego rzutu.
print(f'Sum of dice rolled: {total}')  # Wyświetla sumę trzech wyników.
