# Zadanie 3.6: odległość do horyzontu ze wzoru d = 3.57 * pierwiastek z h.
# Wpisz swój wzrost w metrach, aby obliczyć przypadek stania na plaży.
# Przykład do sprawdzenia: dla wzrostu 1.75 m otrzymasz około 4.72 km.

import math  # Udostępnia funkcję sqrt() obliczającą pierwiastek kwadratowy.

height = float(input("Podaj wysokość obserwatora w metrach: "))  # Pobiera wysokość jako liczbę; część ułamkową wpisz po kropce.
distance = 3.57 * math.sqrt(height)  # Mnoży pierwiastek z wysokości w metrach przez współczynnik 3.57.
print(f"Odległość do horyzontu: {distance:.2f} km")  # Wyświetla odległość w kilometrach z dwoma miejscami po przecinku.

hotel_height = 20  # Zapisuje wysokość okna hotelowego podaną w drugim przypadku zadania.
hotel_distance = 3.57 * math.sqrt(hotel_height)  # Oblicza odległość do horyzontu z wysokości 20 metrów.
print(f"Z okna na wysokości 20 m: {hotel_distance:.2f} km")  # Wyświetla wynik dla hotelu: około 15.97 km.
