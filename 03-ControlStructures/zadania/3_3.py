# Zadanie 3.3: zniżka dla osób poniżej 18 lat lub od 65 lat.
# Przykłady: 72, 65 i 17 -> zniżka; 64 i 18 -> brak zniżki.
age = int(input('Enter your age: '))  # Pobiera wiek jako liczbę całkowitą.
if age < 18 or age >= 65:  # Sprawdza, czy jest spełniony przynajmniej jeden warunek uprawniający do zniżki.
    print('Discount is available')  # Informuje o dostępnej zniżce.
else:  # Wybiera tę część dla wieku od 18 do 64 lat włącznie.
    print('Discount is not available')  # Informuje o braku zniżki.
