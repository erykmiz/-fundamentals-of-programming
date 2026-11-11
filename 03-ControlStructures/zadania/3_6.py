# Zadanie 3.6: sprawdzenie numeru dnia w miesiącu; luty ma tutaj 28 dni.
# Przykłady: miesiąc 3 i dzień 17 -> poprawny; 9 i 31 -> błędny; 2 i 30 -> błędny.
month = int(input('Enter month number (1..12): '))  # Pobiera numer miesiąca.
day = int(input('Enter the day number of the month: '))  # Pobiera numer dnia.
day_ok = False  # Początkowo przyjmuje, że data nie została uznana za poprawną.
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:  # Rozpoznaje miesiące z 31 dniami.
    if day >= 1 and day <= 31:  # Wymaga numeru dnia od 1 do 31 włącznie.
        day_ok = True  # Zapisuje informację o poprawnym dniu.
elif month == 4 or month == 6 or month == 9 or month == 11:  # Rozpoznaje miesiące z 30 dniami.
    if day >= 1 and day <= 30:  # Wymaga numeru dnia od 1 do 30 włącznie.
        day_ok = True  # Uznaje numer dnia za poprawny.
elif month == 2:  # Rozpoznaje luty.
    if day >= 1 and day <= 28:  # Sprawdza zakres od 1 do 28 bez uwzględniania lat przestępnych.
        day_ok = True  # Uznaje numer dnia lutego za poprawny.
message = f'Day {day} for the month {month}'  # Przygotowuje wspólną część komunikatu.
if day_ok:  # Sprawdza, czy numer dnia pasuje do miesiąca.
    print(f'{message} is correct')  # Wyświetla potwierdzenie poprawności.
else:  # Obsługuje błędny dzień lub błędny numer miesiąca.
    print(f'{message} is incorrect')  # Wyświetla informację o niepoprawnej dacie.
