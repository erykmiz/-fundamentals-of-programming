# Zadanie 3.6: sprawdzenie numeru dnia w miesiącu; luty ma tutaj 28 dni.
# Wcięty if sprawdza dzień dopiero po rozpoznaniu rodzaju miesiąca.

month = int(input('Enter month number (1..12): '))  # Pobiera numer miesiąca.
day = int(input('Enter the day number of the month: '))  # Pobiera numer dnia.
day_ok = False  # Na początku zapisuje False, czyli brak potwierdzenia daty.
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:  # Rozpoznaje miesiące z 31 dniami.
    if day >= 1 and day <= 31:  # and wymaga dnia co najmniej 1 i najwyżej 31.
        day_ok = True  # Zapisuje True, bo dzień jest poprawny.
elif month == 4 or month == 6 or month == 9 or month == 11:  # Rozpoznaje miesiące z 30 dniami.
    if day >= 1 and day <= 30:  # Sprawdza dzień od 1 do 30 włącznie.
        day_ok = True  # Potwierdza poprawny dzień.
elif month == 2:  # Rozpoznaje luty.
    if day >= 1 and day <= 28:  # Sprawdza dzień od 1 do 28 zgodnie z założeniem zadania.
        day_ok = True  # Potwierdza poprawny dzień lutego.
message = f'Day {day} for the month {month}'  # f wstawia dzień i miesiąc do wspólnego początku wiadomości.
if day_ok:  # Sprawdza, czy dzień został uznany za poprawny.
    print(f'{message} is correct')  # Pokazuje potwierdzenie poprawnej daty.
else:  # Obsługuje błędny dzień albo miesiąc.
    print(f'{message} is incorrect')  # Pokazuje informację o niepoprawnej dacie.
