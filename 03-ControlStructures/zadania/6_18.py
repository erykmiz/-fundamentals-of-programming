# Zadanie 6.18: Sprawdzamy położenie punktu na płaszczyźnie.
# and wymaga obu warunków; :g pokazuje np. 5 zamiast 5.0.

x = float(input('x = '))  # Pobiera współrzędną poziomą x.
y = float(input('y = '))  # Pobiera współrzędną pionową y.
if x == 0 and y == 0:  # Sprawdza, czy obie współrzędne są zerami.
    location = 'the origin (0,0)'  # Zapisuje położenie w początku układu.
elif y == 0:  # Sprawdza, czy y wynosi 0.
    location = 'the x-axis'  # Zapisuje położenie na osi x.
elif x == 0:  # Sprawdza, czy x wynosi 0.
    location = 'the y-axis'  # Zapisuje położenie na osi y.
elif x > 0 and y > 0:  # Sprawdza, czy x i y są dodatnie.
    location = 'the first quadrant'  # Wybiera pierwszą ćwiartkę.
elif x < 0 and y > 0:  # Sprawdza, czy x jest ujemne, a y dodatnie.
    location = 'the second quadrant'  # Wybiera drugą ćwiartkę.
elif x < 0 and y < 0:  # Sprawdza, czy x i y są ujemne.
    location = 'the third quadrant'  # Wybiera trzecią ćwiartkę.
else:  # Obsługuje pozostały przypadek: dodatnie x i ujemne y.
    location = 'the fourth quadrant'  # Wybiera czwartą ćwiartkę.
print(f'Point P({x:g},{y:g}) is in {location} of the coordinate system')  # Pokazuje współrzędne i położenie punktu.
