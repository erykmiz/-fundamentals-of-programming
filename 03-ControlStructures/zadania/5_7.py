# Zadanie 5.7: odliczanie, którego ostatnie pięć sekund jest zapisane słowami.
import time  # Udostępnia funkcję sleep() zatrzymującą program na wybrany czas.
countdown = int(input("Enter the number of seconds to count down: "))  # Pobiera liczbę sekund jako liczbę całkowitą.
while countdown > 0:  # Powtarza odliczanie, dopóki pozostała przynajmniej jedna sekunda.
    if countdown == 5:  # Sprawdza, czy do końca zostało pięć sekund.
        print("five")  # Wyświetla słowo five zamiast cyfry 5.
    elif countdown == 4:  # Sprawdza, czy zostały cztery sekundy.
        print("four")  # Wyświetla słowo four zamiast cyfry 4.
    elif countdown == 3:  # Sprawdza, czy zostały trzy sekundy.
        print("three")  # Wyświetla słowo three zamiast cyfry 3.
    elif countdown == 2:  # Sprawdza, czy zostały dwie sekundy.
        print("two")  # Wyświetla słowo two zamiast cyfry 2.
    elif countdown == 1:  # Sprawdza, czy została ostatnia sekunda.
        print("one")  # Wyświetla słowo one zamiast cyfry 1.
    else:  # Obsługuje wcześniejsze sekundy, których liczba jest większa niż pięć.
        print(countdown)  # Wyświetla liczbę sekund w zwykłym zapisie liczbowym.
    countdown -= 1  # Zmniejsza pozostały czas o jedną sekundę.
    time.sleep(1)  # Czeka jedną sekundę przed następnym powtórzeniem lub zakończeniem.
print("Time's up!")  # Informuje o zakończeniu odliczania.
