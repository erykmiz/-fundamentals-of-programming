# Zadanie 6.6: opłata parkingowa zależna od liczby pełnych godzin.

hours = int(input('Enter number of parking hours: '))  # Pobiera liczbę pełnych godzin parkowania.
fee = None  # None oznacza, że opłata nie została jeszcze ustalona.
if hours < 0:  # Sprawdza, czy liczba godzin jest ujemna.
    print('Incorrect number of hours')  # Pokazuje informację o błędnej wartości.
elif hours == 0:  # Sprawdza brak czasu parkowania.
    fee = 0  # Zapisuje opłatę 0 za 0 godzin.
elif hours <= 2:  # Po wcześniejszych warunkach pozostają godziny 1-2.
    fee = 5  # Zapisuje opłatę 5 PLN.
elif hours <= 6:  # Sprawdza pozostały przedział 3-6 godzin.
    fee = 15  # Zapisuje opłatę 15 PLN.
else:  # Pozostaje parkowanie dłuższe niż 6 godzin.
    fee = 20  # Zapisuje opłatę 20 PLN.
if fee is not None:  # Sprawdza, czy opłata istnieje; także 0 jest poprawnym wynikiem.
    print(f'Parking fee: {fee} PLN')  # f wstawia obliczoną opłatę w miejsce {fee}.
