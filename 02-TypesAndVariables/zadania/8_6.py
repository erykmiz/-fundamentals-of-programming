# Zadanie 8.6: koszt paliwa zużytego na transport towaru.

distance = int(input('Enter distance in km: '))  # Wczytuje długość trasy w pełnych kilometrach, tak jak w szkielecie zadania.
fuel_price = float(input('Enter fuel price per liter: '))  # Wczytuje cenę jednego litra paliwa.
fuel_consumption = float(input('Enter fuel consumption in liters per 100 km: '))  # Wczytuje liczbę litrów zużywanych na każde 100 km.
total_fuel_consumption = distance / 100 * fuel_consumption  # Oblicza liczbę litrów paliwa potrzebną na całą trasę.
total_cost = total_fuel_consumption * fuel_price  # Mnoży zużyte litry przez cenę jednego litra.
print(f'Total fuel consumption: {total_fuel_consumption:.2f} liters')  # Wyświetla całkowite zużycie paliwa z dwiema cyframi po kropce.
print(f'Total transport cost: {total_cost:.2f}')  # Wyświetla koszt paliwa na trasie z dwiema cyframi po kropce.
