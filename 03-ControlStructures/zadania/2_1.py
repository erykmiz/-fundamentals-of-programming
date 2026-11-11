# Zadanie 2.1: przykład wyboru jednej z kilku możliwości za pomocą elif.
number = 0  # Zapisuje przykładową liczbę; zmień ją na dodatnią lub ujemną, aby sprawdzić inne gałęzie.
if number > 0:  # Sprawdza pierwszy warunek: czy liczba jest dodatnia.
    print('The number is positive')  # Wykonuje tę linię, jeśli pierwszy warunek jest prawdziwy.
elif number < 0:  # Sprawdza drugi warunek tylko wtedy, gdy pierwszy był fałszywy.
    print('The number is negative')  # Wyświetla komunikat dla liczby ujemnej.
else:  # Wybiera tę część, gdy żaden wcześniejszy warunek nie został spełniony.
    print('The number is zero')  # Wyświetla komunikat dla liczby równej 0.
