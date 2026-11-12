# Zadanie 1.3: sprawdzenie przekroczenia limitu podanego w ćwiczeniu.

speed_limit = 140  # Zapisuje limit z zadania: 140 km/h.
car_speed = int(input('Enter car speed (km/h): '))  # input pyta o prędkość, a int zamienia odpowiedź na liczbę.
if car_speed > speed_limit:  # Sprawdza, czy prędkość przekracza limit; samo 140 go nie przekracza.
    print(f'Your speed is {car_speed}km/h')  # f wstawia prędkość w miejsce {car_speed} i pokazuje zdanie.
    print('Warning: speed limit exceeded!!')  # Pokazuje ostrzeżenie tylko po przekroczeniu limitu.
