# Zadanie 2.5: kwartał roku na podstawie numeru miesiąca.
# Przykłady: miesiąc 12 -> kwartał 4; 10 -> 4; 9 -> 3; 1 -> 1.
month = int(input('Enter month number (1..12): '))  # Pobiera numer miesiąca jako liczbę całkowitą.
quarter = 0  # Ustawia 0 jako informację, że nie wybrano jeszcze poprawnego kwartału.
if month < 1 or month > 12:  # Sprawdza, czy numer miesiąca wykracza poza zakres od 1 do 12.
    print('Incorrect month number')  # Informuje o niepoprawnym numerze miesiąca.
elif month >= 10:  # Sprawdza miesiące 10, 11 i 12, czyli czwarty kwartał.
    quarter = 4  # Zapisuje numer czwartego kwartału.
elif month >= 7:  # Po wykluczeniu miesięcy od 10 wzwyż sprawdza miesiące 7, 8 i 9.
    quarter = 3  # Zapisuje numer trzeciego kwartału.
elif month >= 4:  # Sprawdza miesiące 4, 5 i 6.
    quarter = 2  # Zapisuje numer drugiego kwartału.
else:  # Pozostają poprawne miesiące 1, 2 i 3.
    quarter = 1  # Zapisuje numer pierwszego kwartału.
if quarter > 0:  # Wyświetla wynik tylko dla poprawnego numeru miesiąca.
    print(f'Month {month} is in quarter {quarter}')  # Pokazuje numer miesiąca i wyznaczony kwartał.
