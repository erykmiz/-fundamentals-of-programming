# Zadanie 1.4: udajemy pięć rzutów zwykłą kostką, losując liczby od 1 do 6.

import random  # import udostępnia gotowy moduł random, czyli zestaw narzędzi do losowania.

print("Dice rolling simulator")  # print pokazuje tytuł programu zapisany jako tekst w cudzysłowie.
for i in range(5):  # Powtarza wcięte linie 5 razy; range(5) daje liczby od 0 do 4.
    dice_roll = random.randint(1, 6)  # randint losuje liczbę całkowitą od 1 do 6 włącznie; = zapisuje ją w dice_roll.
    print(dice_roll, end=" ")  # Pokazuje wylosowaną liczbę; end=" " dopisuje spację zamiast przejścia do nowej linii.
print()  # Ta linia nie jest wcięta, więc wykona się raz po pętli i przejdzie do nowej linii.
