# Zadanie 5.4: odgadywanie wylosowanej liczby od 1 do 100.
import random  # Udostępnia funkcję losującą liczbę do odgadnięcia.
number_to_guess = random.randint(1, 100)  # Losuje liczbę całkowitą z przedziału od 1 do 100 włącznie.
user_guess = 0  # Ustawia początkowy typ poza zakresem losowania, aby rozpocząć pętlę.
print("Guess the number between 1 and 100!")  # Wyświetla cel gry i dostępny zakres liczb.
while user_guess != number_to_guess:  # Powtarza zgadywanie, dopóki podana liczba nie zgadza się z wylosowaną.
    user_guess = int(input("Enter your guess: "))  # Wczytuje kolejną próbę i zamienia tekst na liczbę całkowitą.
    if user_guess < number_to_guess:  # Sprawdza, czy podana liczba jest za mała.
        print("Too low! Try again.")  # Podpowiada, aby przy następnej próbie wybrać większą liczbę.
    elif user_guess > number_to_guess:  # Sprawdza, czy podana liczba jest za duża.
        print("Too high! Try again.")  # Podpowiada, aby przy następnej próbie wybrać mniejszą liczbę.
    else:  # Pozostaje przypadek, w którym obie liczby są równe.
        print("Congratulations! You guessed the correct number.")  # Informuje o trafieniu; następne sprawdzenie warunku zakończy pętlę.
