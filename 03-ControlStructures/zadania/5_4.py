# Zadanie 5.4: zgadujemy wylosowaną liczbę.
# != oznacza „różne od”; int(input(...)) zamienia wpisany tekst na liczbę.

import random  # Udostępnia narzędzia do losowania.
number_to_guess = random.randint(1, 100)  # Losuje liczbę całkowitą od 1 do 100 włącznie.
user_guess = 0  # Zapisuje 0, które różni się od wylosowanej liczby.
print("Guess the number between 1 and 100!")  # Pokazuje zasady gry.
while user_guess != number_to_guess:  # Ponawia zgadywanie, dopóki liczby są różne.
    user_guess = int(input("Enter your guess: "))  # Pobiera próbę i zamienia tekst na liczbę całkowitą.
    if user_guess < number_to_guess:  # Sprawdza, czy próba jest za mała.
        print("Too low! Try again.")  # Podpowiada, aby wybrać większą liczbę.
    elif user_guess > number_to_guess:  # Sprawdza, czy próba jest za duża.
        print("Too high! Try again.")  # Podpowiada, aby wybrać mniejszą liczbę.
    else:  # Pozostaje przypadek trafienia.
        print("Congratulations! You guessed the correct number.")  # Pokazuje sukces; warunek while zakończy pętlę.
