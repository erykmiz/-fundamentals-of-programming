# Zadanie 6.13: Sprawdzamy zakres prędkości z ćwiczenia: 40–140 km/h.
# or znaczy „lub”; ostrzeżenie wystarczy po spełnieniu jednego z warunków.

car_speed = float(input('Enter car speed: '))  # Pobiera prędkość i zamienia tekst na liczbę.
speed_limit_min = 40  # Ustawia dolną granicę: 40 km/h.
speed_limit_max = 140  # Ustawia górną granicę: 140 km/h.
if car_speed < speed_limit_min or car_speed > speed_limit_max:  # Sprawdza, czy prędkość jest mniejsza od 40 lub większa od 140.
    print('Warning: invalid car speed!!')  # Pokazuje ostrzeżenie o prędkości poza zakresem.
