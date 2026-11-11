# Zadanie 1.3: sprawdzenie przekroczenia limitu podanego w ćwiczeniu.
speed_limit = 140  # Zapisuje limit 140 km/h przyjęty w treści zadania.
car_speed = int(input('Enter car speed (km/h): '))  # Pobiera prędkość i zamienia tekst na liczbę całkowitą.
if car_speed > speed_limit:  # Sprawdza, czy podana prędkość jest większa od limitu.
    print(f'Your speed is {car_speed}km/h')  # Wyświetla prędkość kierowcy, jeśli przekroczył limit.
    print('Warning: speed limit exceeded!!')  # Wyświetla ostrzeżenie tylko po przekroczeniu limitu.
