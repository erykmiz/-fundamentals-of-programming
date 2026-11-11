# Zadanie 7.9: losujemy rzut kostką i sprawdzamy, czy wypadło 1 lub 6.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

import random  # Udostępnia moduł random potrzebny do losowania.
dice_roll = random.randint(1, 6)  # Wybiera losowo jedną liczbę od 1 do 6 włącznie i zapisuje wynik rzutu.
special_number = dice_roll == 1 or dice_roll == 6  # Zapisuje True, jeśli rzut dał 1 albo 6; dla 2, 3, 4 i 5 zapisuje False.
print(f'Dice rolled: {dice_roll}')  # Pokazuje, ile oczek naprawdę wypadło w losowaniu.
print(f'Special number (1 or 6): {special_number}')  # Pokazuje True dla wyniku specjalnego albo False dla pozostałych wyników.
