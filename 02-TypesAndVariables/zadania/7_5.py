# Zadanie 7.5: sprawdzamy, czy numer rejestracyjny zaczyna się od KR albo KK.
# strip() usuwa skrajne spacje, upper() zmienia litery na wielkie.
# [0:2] bierze pierwsze 2 znaki; or wymaga spełnienia choć jednego warunku.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

car_number = input('Enter car registration number: ').strip().upper()  # Pobiera i porządkuje zapis numeru, a potem zapamiętuje go jako car_number.
is_krakow = car_number[0:2] == 'KR' or car_number[0:2] == 'KK'  # Sprawdza dwa pierwsze znaki i zapisuje True dla KR albo KK, inaczej False.
print(f'Car is from Krakow: {is_krakow}')  # Wyświetla odpowiedź, czy numer ma jeden z dwóch początków podanych w ćwiczeniu.
