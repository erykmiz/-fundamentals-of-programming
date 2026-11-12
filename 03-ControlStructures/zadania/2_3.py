# Zadanie 2.3: zużycie paliwa dla trybów Auto, Manual i Eco.
# f wstawia wartości z {}; :g daje zwięzły zapis liczby, np. 18 zamiast 18.0.

driving_mode = input('Enter driving mode (A/M/E): ').strip().upper()  # Pobiera tryb i zamienia litery na wielkie, np. m na M.
distance = int(input('Enter distance in km: '))  # Pobiera długość trasy w pełnych kilometrach.
fuel_consumption = 0  # Przygotowuje spalanie; 0 oznacza, że nie wybrano poprawnego trybu.
if driving_mode == 'A':  # Sprawdza tryb Auto.
    fuel_consumption = 7  # Ustawia 7 litrów na 100 km.
elif driving_mode == 'M':  # Sprawdza tryb Manual.
    fuel_consumption = 9  # Ustawia 9 litrów na 100 km.
elif driving_mode == 'E':  # Sprawdza tryb Eco.
    fuel_consumption = 6  # Ustawia 6 litrów na 100 km.
else:  # Obsługuje symbol inny niż A, M lub E.
    print('Incorrect driving mode')  # Pokazuje informację o błędnym trybie.
if fuel_consumption > 0:  # Liczy wynik tylko dla poprawnego trybu, który ma spalanie większe od 0.
    total_consumption = distance / 100 * fuel_consumption  # Liczy paliwo na całą trasę, np. 200 / 100 * 9 = 18 litrów.
    print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption:g} liters')  # Pokazuje trasę, tryb i liczbę zużytych litrów.
