# Zadanie 6.21: Rozmieniamy kwotę na możliwie najmniej monet 5, 2 i 1 PLN.
# // liczy pełne monety danego nominału, a % kwotę pozostałą po ich odjęciu.

amount = int(input('Enter the amount in PLN: '))  # Pobiera kwotę w pełnych złotych.
if amount < 0:  # Sprawdza, czy kwota jest ujemna.
    print('The amount cannot be negative.')  # Informuje o błędnej kwocie.
else:  # Obsługuje kwotę nieujemną.
    coins_5 = amount // 5  # Liczy pełne monety po 5 PLN.
    remaining = amount % 5  # Liczy resztę po monetach pięciozłotowych.
    coins_2 = remaining // 2  # Z reszty liczy pełne monety po 2 PLN.
    coins_1 = remaining % 2  # Pozostałe 0 lub 1 PLN wydaje monetami po 1 PLN.
    print(f'The amount of PLN {amount} in coins:')  # Pokazuje rozmienianą kwotę.
    print(f'5 PLN coins: {coins_5}')  # Pokazuje liczbę monet po 5 PLN.
    print(f'2 PLN coins: {coins_2}')  # Pokazuje liczbę monet po 2 PLN.
    print(f'1 PLN coins: {coins_1}')  # Pokazuje liczbę monet po 1 PLN.
