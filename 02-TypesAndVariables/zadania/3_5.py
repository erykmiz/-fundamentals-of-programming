# Zadanie 3.5: obliczamy długość przekątnej prostokąta o bokach 5 i 8.
# ** 2 to kwadrat; math.sqrt liczy pierwiastek, np. sqrt(9) = 3, bo 3 * 3 = 9.

import math  # Udostępnia moduł math, czyli gotowe narzędzia matematyczne, w tym funkcję sqrt.

a = 5  # Zapisuje długość pierwszego boku: 5; = oznacza zapamiętanie wartości pod nazwą a.
b = 8  # Zapisuje długość drugiego boku: 8.
diagonal = math.sqrt(a ** 2 + b ** 2)  # Liczy 25 + 64 = 89, potem pierwiastek z 89 i zapisuje około 9.43398.
print("Przekątna prostokąta:", diagonal)  # print pokazuje podpis i wynik zapamiętany w diagonal.
