# Zadanie 3.6: liczymy przybliżoną odległość do horyzontu z wysokości podanej w metrach.
# math.sqrt liczy pierwiastek; wysokość wpisuj w metrach z kropką, np. 1.75.
# f wstawia wartości z {}; :.2f pokazuje 2 miejsca po kropce, bez zmiany wartości zmiennej.

import math  # Udostępnia moduł math; użyjemy z niego sqrt, czyli funkcji liczącej pierwiastek kwadratowy.

height = float(input("Podaj wysokość obserwatora w metrach: "))  # Wczytuje wysokość jako liczbę i zapisuje ją pod nazwą height.
distance = 3.57 * math.sqrt(height)  # Najpierw liczy pierwiastek z height, potem mnoży przez 3.57 i zapisuje odległość w km.
print(f"Odległość do horyzontu: {distance:.2f} km")  # Pokazuje podpis, obliczoną odległość i jednostkę km, np. 4.72 km.

hotel_height = 20  # = zapisuje pod nazwą hotel_height wysokość okna hotelowego: 20 metrów.
hotel_distance = 3.57 * math.sqrt(hotel_height)  # Używa tego samego wzoru dla 20 m; wynik wynosi około 15.97 km.
print(f"Z okna na wysokości 20 m: {hotel_distance:.2f} km")  # Pokazuje wynik dla hotelu z dwiema cyframi po kropce.
