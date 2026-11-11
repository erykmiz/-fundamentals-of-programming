# Zadanie 7.6: sprawdzamy, czy prędkość mieści się w przedziale od 40 do 140 km/h włącznie.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

speed = float(input('Enter vehicle speed: '))  # Pyta o prędkość i zapisuje ją jako liczbę pod nazwą speed.
speed_is_valid = 40 <= speed <= 140  # Sprawdza 40 <= speed oraz speed <= 140; dla 100 wynik to True, a dla 158 False.
print(f'Speed is valid: {speed_is_valid}')  # Pokazuje wynik sprawdzenia podanej prędkości.
