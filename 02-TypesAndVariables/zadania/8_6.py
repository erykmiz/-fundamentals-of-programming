# Zadanie 8.6: liczymy ilość paliwa potrzebnego na trasę i koszt tego paliwa.
# f wstawia wartości z {}; :.2f pokazuje 2 miejsca po kropce, bez zmiany wartości zmiennej.

distance = int(input('Enter distance in km: '))  # Pyta o dystans w pełnych kilometrach i zapisuje liczbę jako distance.
fuel_price = float(input('Enter fuel price per liter: '))  # Pyta o cenę jednego litra, np. 6.5, i zapisuje ją jako liczbę.
fuel_consumption = float(input('Enter fuel consumption in liters per 100 km: '))  # Pyta o spalanie, np. 7 litrów na 100 km.
total_fuel_consumption = distance / 100 * fuel_consumption  # Dla przykładu liczy 200 / 100 * 7, czyli 14 litrów paliwa.
total_cost = total_fuel_consumption * fuel_price  # Mnoży liczbę potrzebnych litrów przez cenę litra; 14 * 6.5 daje koszt 91.
print(f'Total fuel consumption: {total_fuel_consumption:.2f} liters')  # Wyświetla ilość paliwa, np. 14.00 liters dla przykładu.
print(f'Total transport cost: {total_cost:.2f}')  # Wyświetla koszt paliwa na trasie, np. 91.00 dla przykładu.
