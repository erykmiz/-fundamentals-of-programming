# Zadanie 7.8: wykonujemy trzy rzuty kostką i dodajemy liczbę oczek.
# randint(1, 6) losuje od 1 do 6 włącznie; kolejne wyniki mogą się powtarzać.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

import random  # Udostępnia moduł random, z którego użyjemy funkcji losującej randint.
dice_roll_1 = random.randint(1, 6)  # Losuje od 1 do 6 włącznie i zapisuje pierwszy rzut pod nazwą dice_roll_1.
dice_roll_2 = random.randint(1, 6)  # Wykonuje osobne losowanie drugiego rzutu; jego wynik może być taki sam jak pierwszego.
dice_roll_3 = random.randint(1, 6)  # Wykonuje trzecie losowanie i zapamiętuje je osobno.
total = dice_roll_1 + dice_roll_2 + dice_roll_3  # Dodaje wszystkie trzy zapamiętane wyniki; np. 1 + 6 + 3 daje sumę 10.
print(f'Dice rolls: {dice_roll_1}, {dice_roll_2}, {dice_roll_3}')  # Pokazuje trzy osobne wyniki, wstawiając każdy w jego nawiasy klamrowe.
print(f'Sum of dice rolled: {total}')  # Pokazuje sumę oczek zapisaną w total.
