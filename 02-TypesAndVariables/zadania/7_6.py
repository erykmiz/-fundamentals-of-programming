# Zadanie 7.6: sprawdzenie przedziału prędkości podanego w ćwiczeniu.
# Granice należą do przedziału: 40 i 140 dają True, a 158 daje False.

speed = float(input('Enter vehicle speed: '))  # Wczytuje prędkość pojazdu w kilometrach na godzinę.
speed_is_valid = 40 <= speed <= 140  # Sprawdza jednocześnie, czy prędkość wynosi co najmniej 40 i najwyżej 140.
print(f'Speed is valid: {speed_is_valid}')  # Wyświetla wynik sprawdzenia zakresu prędkości.
