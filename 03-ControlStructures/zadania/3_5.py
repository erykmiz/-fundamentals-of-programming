# Zadanie 3.5: liczba dni w miesiącu; zgodnie z poleceniem luty ma zawsze 28 dni.
month = int(input('Enter month number (1..12): '))  # Pobiera numer miesiąca.
days = 0  # Przygotowuje liczbę dni; 0 będzie oznaczać błędny numer miesiąca.
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:  # Rozpoznaje miesiące mające 31 dni.
    days = 31  # Ustawia liczbę dni dla jednego z wymienionych miesięcy.
elif month == 4 or month == 6 or month == 9 or month == 11:  # Rozpoznaje miesiące mające 30 dni.
    days = 30  # Ustawia liczbę dni dla miesiąca trzydziestodniowego.
elif month == 2:  # Rozpoznaje luty.
    days = 28  # Przyjmuje 28 dni bez sprawdzania lat przestępnych, zgodnie z poleceniem.
else:  # Obsługuje numer miesiąca inny niż od 1 do 12.
    print('Incorrect month number')  # Informuje o niepoprawnym numerze.
if days > 0:  # Wyświetla wynik tylko dla poprawnego miesiąca.
    print(f'Month {month} has {days} days')  # Pokazuje numer miesiąca i jego liczbę dni.
