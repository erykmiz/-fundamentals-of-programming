# Zadanie 3.5: liczba dni w miesiącu; zgodnie z poleceniem luty ma zawsze 28 dni.

month = int(input('Enter month number (1..12): '))  # Pobiera numer miesiąca.
days = 0  # Przygotowuje liczbę dni; 0 oznacza błędny numer miesiąca.
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:  # or pozwala rozpoznać dowolny z wymienionych miesięcy z 31 dniami.
    days = 31  # Zapisuje 31 dni.
elif month == 4 or month == 6 or month == 9 or month == 11:  # Sprawdza miesiące z 30 dniami.
    days = 30  # Zapisuje 30 dni.
elif month == 2:  # Sprawdza luty, czyli miesiąc numer 2.
    days = 28  # Zapisuje 28 dni, zgodnie z założeniem zadania.
else:  # Obsługuje numer spoza 1-12.
    print('Incorrect month number')  # Pokazuje informację o błędnym miesiącu.
if days > 0:  # Pokazuje wynik tylko dla poprawnego numeru miesiąca.
    print(f'Month {month} has {days} days')  # f wstawia numer miesiąca i liczbę dni w miejsca {}.
