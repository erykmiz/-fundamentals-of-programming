# Zadanie 6.6: opłata parkingowa zależna od liczby pełnych godzin.
# Dla 0 godzin przyjmujemy brak opłaty; ujemna liczba godzin jest niepoprawna.
hours = int(input('Enter number of parking hours: '))  # Pobiera liczbę pełnych godzin parkowania.
fee = None  # Przyjmuje brak obliczonej opłaty, dopóki nie sprawdzi podanej liczby godzin.
if hours < 0:  # Sprawdza, czy wpisano niemożliwą ujemną liczbę godzin.
    print('Incorrect number of hours')  # Informuje o niepoprawnej wartości.
elif hours == 0:  # Sprawdza przypadek braku czasu parkowania.
    fee = 0  # Przyjmuje opłatę 0 za 0 godzin.
elif hours <= 2:  # Po wykluczeniu zera i liczb ujemnych pozostają godziny 1 i 2.
    fee = 5  # Ustawia opłatę 5 PLN za 1–2 godziny.
elif hours <= 6:  # Sprawdza przedział od 3 do 6 godzin włącznie.
    fee = 15  # Ustawia opłatę 15 PLN.
else:  # Pozostają wartości większe niż 6 godzin.
    fee = 20  # Ustawia opłatę 20 PLN.
if fee is not None:  # Wyświetla opłatę tylko dla poprawnej liczby godzin.
    print(f'Parking fee: {fee} PLN')  # Pokazuje obliczoną kwotę do zapłaty.
