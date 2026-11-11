# Zadanie 6.18: położenie punktu na płaszczyźnie.
x = float(input('x = '))  # Wczytuje współrzędną poziomą punktu.
y = float(input('y = '))  # Wczytuje współrzędną pionową punktu.
if x == 0 and y == 0:  # Sprawdza jednocześnie obie współrzędne, aby rozpoznać początek układu.
    location = 'the origin (0,0)'  # Zapisuje opis początku układu współrzędnych.
elif y == 0:  # Rozpoznaje oś poziomą; początek układu został już wykluczony.
    location = 'the x-axis'  # Zapisuje opis osi x.
elif x == 0:  # Rozpoznaje oś pionową; początek układu został już wykluczony.
    location = 'the y-axis'  # Zapisuje opis osi y.
elif x > 0 and y > 0:  # Sprawdza, czy obie współrzędne są dodatnie.
    location = 'the first quadrant'  # Przypisuje punkt do pierwszej ćwiartki.
elif x < 0 and y > 0:  # Sprawdza, czy x jest ujemne, a y dodatnie.
    location = 'the second quadrant'  # Przypisuje punkt do drugiej ćwiartki.
elif x < 0 and y < 0:  # Sprawdza, czy obie współrzędne są ujemne.
    location = 'the third quadrant'  # Przypisuje punkt do trzeciej ćwiartki.
else:  # Pozostał przypadek dodatniego x i ujemnego y.
    location = 'the fourth quadrant'  # Przypisuje punkt do czwartej ćwiartki.
print(f'Point P({x:g},{y:g}) is in {location} of the coordinate system')  # Wyświetla punkt i opis jego położenia.
