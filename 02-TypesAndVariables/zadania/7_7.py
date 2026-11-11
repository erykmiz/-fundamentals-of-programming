# Zadanie 7.7: losujemy pięć liczb całkowitych od 5 do 10.
# range(5) daje 0, 1, 2, 3, 4; losowane wyniki mogą się powtarzać.

import random  # Udostępnia moduł random, czyli zestaw narzędzi do losowania liczb.
for i in range(5):  # Wykonuje wcięte linie pięć razy; w każdym powtórzeniu i otrzymuje kolejną wartość z range(5).
    random_number = random.randint(5, 10)  # Losuje jedną liczbę: 5, 6, 7, 8, 9 lub 10, i zapisuje ją w random_number.
    print(random_number)  # Wyświetla wynik bieżącego losowania; zwykłe print przechodzi potem do nowej linii.
