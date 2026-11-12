# Zadanie 2.5: kwartał roku na podstawie numeru miesiąca.

month = int(input('Enter month number (1..12): '))  # Pobiera numer miesiąca jako liczbę całkowitą.
quarter = 0  # Przygotowuje kwartał; 0 oznacza brak poprawnego wyniku.
if month < 1 or month > 12:  # or oznacza lub; odrzuca numery mniejsze od 1 albo większe od 12.
    print('Incorrect month number')  # Pokazuje informację o błędnym miesiącu.
elif month >= 10:  # Po wykluczeniu błędnych numerów sprawdza miesiące 10-12.
    quarter = 4  # Zapisuje czwarty kwartał.
elif month >= 7:  # Sprawdza pozostałe miesiące 7-9.
    quarter = 3  # Zapisuje trzeci kwartał.
elif month >= 4:  # Sprawdza pozostałe miesiące 4-6.
    quarter = 2  # Zapisuje drugi kwartał.
else:  # Pozostają poprawne miesiące 1-3.
    quarter = 1  # Zapisuje pierwszy kwartał.
if quarter > 0:  # Pokazuje wynik tylko po ustaleniu poprawnego kwartału.
    print(f'Month {month} is in quarter {quarter}')  # f wstawia wartości z {} i pokazuje miesiąc oraz kwartał.
