# Zadanie 6.31: Losujemy 20 liczb całkowitych od 5 do 10.
# range(20) daje 20 powtórzeń; randint uwzględnia obie granice, a wyniki mogą się powtarzać.

import random  # Udostępnia moduł random z funkcją losującą randint.
for index in range(20):  # Powtarza wcięte linie 20 razy.
    number = random.randint(5, 10)  # Losuje liczbę od 5 do 10 włącznie.
    print(number, end=' ')  # Pokazuje wynik i spację zamiast nowej linii.
print()  # Kończy wiersz po 20 losowaniach.
