# Zadanie 7.5: sprawdzenie początku numeru rejestracyjnego.

car_number = input('Enter car registration number: ').strip().upper()  # Wczytuje numer, usuwa skrajne spacje i zamienia litery na wielkie.
is_krakow = car_number[0:2] == 'KR' or car_number[0:2] == 'KK'  # Sprawdza, czy pierwsze dwa znaki to KR lub KK; wystarczy jeden z tych warunków.
print(f'Car is from Krakow: {is_krakow}')  # Wyświetla True, gdy numer spełnia warunek z ćwiczenia.
