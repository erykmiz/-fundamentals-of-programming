# Zadanie 6.28: Wypisujemy pierwszych 20 wyrazów ciągu Fibonacciego.
# Kolejny wyraz jest sumą poprzednich dwóch; next_number zachowuje tę sumę przed zmianą pary.

first = 0  # Zapisuje pierwszy wyraz: 0.
second = 1  # Zapisuje drugi wyraz: 1.
for index in range(20):  # Powtarza wypisywanie dokładnie 20 razy.
    print(first, end=' ')  # Pokazuje bieżący wyraz i spację zamiast nowej linii.
    next_number = first + second  # Dodaje dwa kolejne wyrazy i zachowuje sumę.
    first = second  # Przesuwa drugi wyraz na miejsce pierwszego.
    second = next_number  # Zapisuje obliczoną sumę jako drugi wyraz nowej pary.
print()  # Kończy wiersz po 20 liczbach.
