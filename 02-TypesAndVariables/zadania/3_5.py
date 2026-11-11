# Zadanie 3.5: długość przekątnej prostokąta o bokach 5 i 8.

import math  # Udostępnia funkcje matematyczne, w tym sqrt() do obliczania pierwiastka.

a = 5  # Zapisuje długość pierwszego boku prostokąta.
b = 8  # Zapisuje długość drugiego boku prostokąta.
diagonal = math.sqrt(a ** 2 + b ** 2)  # Z twierdzenia Pitagorasa oblicza pierwiastek z sumy kwadratów boków.
print("Przekątna prostokąta:", diagonal)  # Wyświetla długość przekątnej, około 9.43398.
