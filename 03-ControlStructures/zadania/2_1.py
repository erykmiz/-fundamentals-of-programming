# Zadanie 2.1: przykład wyboru jednej z kilku możliwości za pomocą elif.
# if/elif/else wybierają jedną pasującą możliwość.

number = 0  # Zapisuje przykładowe zero; możesz tu wpisać inną liczbę.
if number > 0:  # Sprawdza, czy liczba jest dodatnia.
    print('The number is positive')  # Pokazuje wiadomość dla liczby większej od zera.
elif number < 0:  # Sprawdza kolejny warunek tylko wtedy, gdy poprzedni był fałszywy.
    print('The number is negative')  # Pokazuje wiadomość dla liczby mniejszej od zera.
else:  # Wybiera tę część, gdy oba wcześniejsze warunki są fałszywe.
    print('The number is zero')  # Pokazuje wiadomość dla zera.
