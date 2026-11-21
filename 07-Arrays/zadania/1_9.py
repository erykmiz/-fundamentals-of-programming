# Zadanie 1.9. Wybieramy rejestracje z Krakowa i numerujemy wyniki.

polish_license_plates = [  # Zapisuje wszystkie podane numery rejestracyjne.
    'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',  # Dodaje numery z pierwszego wiersza.
    'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',  # Dodaje numery z drugiego wiersza.
    'KK54985', 'LU4864U',  # Dopisuje dwa ostatnie numery.
]  # Kończy listę rejestracji.

counter = 1  # Ustawia numer pierwszej pasującej pozycji.
for car_number in polish_license_plates:  # Sprawdza po kolei wszystkie numery rejestracyjne.
    if car_number.startswith(('KR', 'KK')):  # Sprawdza, czy numer zaczyna się od KR albo KK.
        print(f'{counter}. {car_number}')  # Wyświetla numer pozycji i pasującą rejestrację.
        counter += 1  # Zwiększa numer pozycji wyłącznie po wypisaniu pasującej rejestracji.
