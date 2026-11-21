# Zadanie 3.1. Obliczamy pierwiastek, logarytm naturalny i sinus za pomocą modułu math.

import math  # Udostępnia funkcje matematyczne pod nazwą math.

square_root = math.sqrt(7)  # Oblicza pierwiastek kwadratowy z 7.
print('A square root of 7 is', square_root)  # Wyświetla pierwiastek.

natural_logarithm = math.log(5)  # Bez podanej podstawy log oblicza logarytm naturalny.
print('The natural logarithm of 5 is', natural_logarithm)  # Wyświetla logarytm.

angle = math.radians(90)  # Zamienia 90 stopni na radiany wymagane przez sin.
sine = math.sin(angle)  # Oblicza sinus podanego kąta.
print('The sine of 90 degrees is', sine)  # Wyświetla sinus.
