# Zadanie 6.13: sprawdzenie zakresu prędkości podanego w ćwiczeniu.
car_speed = float(input('Enter car speed: '))  # Wczytuje prędkość samochodu jako liczbę.
speed_limit_min = 40  # Zapisuje dolną granicę z treści zadania.
speed_limit_max = 140  # Zapisuje górną granicę z treści zadania.
if car_speed < speed_limit_min or car_speed > speed_limit_max:  # Sprawdza, czy prędkość jest poza przedziałem od 40 do 140 włącznie.
    print('Warning: invalid car speed!!')  # Wyświetla ostrzeżenie, gdy choć jedna z granic jest przekroczona.
