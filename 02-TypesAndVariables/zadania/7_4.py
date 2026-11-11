# Zadanie 7.4: z obwodu drzewa liczymy średnicę i sprawdzamy, czy wynosi przynajmniej 50 cm.
# Obwód koła = pi * średnica, dlatego średnicę liczymy jako obwód / pi.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

import math  # Udostępnia moduł math, czyli zestaw narzędzi matematycznych, z którego bierzemy liczbę pi.
circumference = float(input('Enter tree circumference in cm: '))  # Pyta o obwód w centymetrach i zapisuje go jako liczbę.
diameter = circumference / math.pi  # Dzieli obwód przez pi i zapisuje średnicę; przy obwodzie 160 cm jest to około 50.93 cm.
can_cut_down = diameter >= 50  # >= sprawdza „większe lub równe”; zapisuje True dla średnicy co najmniej 50 cm, inaczej False.
print(f'Tree can be cut down: {can_cut_down}')  # Wyświetla wynik zgodnie z regułą z zadania, np. True dla obwodu 160 cm.
