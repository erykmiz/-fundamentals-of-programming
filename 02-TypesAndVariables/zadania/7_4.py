# Zadanie 7.4: obliczenie średnicy drzewa z obwodu.
# Stosujemy wyłącznie uproszczony warunek średnicy co najmniej 50 cm z treści ćwiczenia.
# Przykłady obwodów w cm: 160 -> True, 90 -> False, 230 -> True, 120 -> False.

import math  # Udostępnia stałą math.pi, czyli przybliżoną wartość liczby pi.
circumference = float(input('Enter tree circumference in cm: '))  # Wczytuje obwód w centymetrach jako liczbę, która może mieć część dziesiętną.
diameter = circumference / math.pi  # Oblicza średnicę ze wzoru: średnica = obwód / pi.
can_cut_down = diameter >= 50  # Sprawdza, czy obliczona średnica wynosi co najmniej 50 cm.
print(f'Tree can be cut down: {can_cut_down}')  # Wyświetla wynik warunku przyjętego w zadaniu.
