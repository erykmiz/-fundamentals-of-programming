# Zadanie 5.7: odliczamy, a ostatnie pięć sekund pokazujemy słowami.
# -= 1 zmniejsza licznik o jeden, a sleep(1) czeka sekundę.

import time  # Udostępnia funkcję sleep() do czekania.
countdown = int(input("Enter the number of seconds to count down: "))  # Pobiera liczbę sekund jako liczbę całkowitą.
while countdown > 0:  # Powtarza odliczanie, dopóki licznik jest dodatni.
    if countdown == 5:  # Sprawdza, czy zostało 5 sekund.
        print("five")  # Pokazuje five, czyli pięć.
    elif countdown == 4:  # Sprawdza, czy zostały 4 sekundy.
        print("four")  # Pokazuje four, czyli cztery.
    elif countdown == 3:  # Sprawdza, czy zostały 3 sekundy.
        print("three")  # Pokazuje three, czyli trzy.
    elif countdown == 2:  # Sprawdza, czy zostały 2 sekundy.
        print("two")  # Pokazuje two, czyli dwa.
    elif countdown == 1:  # Sprawdza, czy została 1 sekunda.
        print("one")  # Pokazuje one, czyli jeden.
    else:  # Obsługuje wartości większe niż 5.
        print(countdown)  # Pokazuje liczbę sekund cyframi.
    countdown -= 1  # Zmniejsza licznik o 1.
    time.sleep(1)  # Czeka 1 sekundę.
print("Time's up!")  # Pokazuje komunikat o końcu odliczania.
