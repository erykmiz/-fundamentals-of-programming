# Zadanie 2.3: zużycie paliwa dla trybów Auto, Manual i Eco.
# Przykłady: M i 200 km -> 18 l; A i 400 km -> 28 l; E i 350 km -> 21 l.
driving_mode = input('Enter driving mode (A/M/E): ').strip().upper()  # Pobiera symbol trybu i zamienia go na wielką literę.
distance = int(input('Enter distance in km: '))  # Pobiera długość trasy w pełnych kilometrach.
fuel_consumption = 0  # Przygotowuje zmienną na zużycie paliwa; 0 oznacza tu nierozpoznany tryb.
if driving_mode == 'A':  # Sprawdza, czy wybrano tryb Auto.
    fuel_consumption = 7  # Ustawia zużycie 7 litrów na 100 km dla trybu Auto.
elif driving_mode == 'M':  # Sprawdza, czy wybrano tryb Manual.
    fuel_consumption = 9  # Ustawia zużycie 9 litrów na 100 km dla trybu Manual.
elif driving_mode == 'E':  # Sprawdza, czy wybrano tryb Eco.
    fuel_consumption = 6  # Ustawia zużycie 6 litrów na 100 km dla trybu Eco.
else:  # Obsługuje symbol trybu inny niż A, M lub E.
    print('Incorrect driving mode')  # Informuje o błędnym symbolu.
if fuel_consumption > 0:  # Oblicza wynik tylko wtedy, gdy wybrano poprawny tryb.
    total_consumption = distance / 100 * fuel_consumption  # Przelicza zużycie na całą podaną trasę.
    print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption:g} liters')  # Wyświetla dystans, tryb oraz obliczoną liczbę litrów.
