# Zadanie 1.4: symulacja pięciu rzutów kostką.
# Uruchom plik w VS Code, aby zobaczyć pięć losowych wyników.

import random  # Udostępnia funkcje służące do losowania liczb.

print("Dice rolling simulator")  # Wyświetla tytuł programu: symulator rzutów kostką.
for i in range(5):  # Powtarza wcięte polecenia pięć razy; i przyjmuje wartości od 0 do 4.
    dice_roll = random.randint(1, 6)  # Losuje liczbę całkowitą od 1 do 6 włącznie, jak na kostce.
    print(dice_roll, end=" ")  # Wyświetla wynik i spację zamiast przejścia do następnej linii.
print()  # Kończy linię po wyświetleniu wszystkich pięciu wyników.
