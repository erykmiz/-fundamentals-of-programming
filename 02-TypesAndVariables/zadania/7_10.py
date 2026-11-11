# Zadanie 7.10: komputer rzuca kostką, a użytkownik próbuje odgadnąć wynik.
# = zapisuje wynik w zmiennej, a == porównuje dwie wartości.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

import random  # Udostępnia moduł random, aby można było użyć funkcji losującej randint.
computer = random.randint(1, 6)  # Losuje liczbę od 1 do 6 włącznie i zapamiętuje ją jako computer, bez wyświetlania jej przed próbą.
you = int(input('Guess the dice number (1-6): '))  # Pobiera Twój typ, zamienia go na liczbę całkowitą i zapisuje pod nazwą you.
you_won = you == computer  # Sprawdza, czy wpisana liczba jest taka sama jak wylosowana; zapisuje True przy trafieniu, inaczej False.
print(f'You won: {you_won}')  # Wyświetla informację o wyniku: True oznacza trafienie, a False nietrafienie.
