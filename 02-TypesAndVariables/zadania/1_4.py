
# Importujemy moduł random, który pozwala losować liczby
import random

# Wyświetlamy napis informujący, co robi program
print("Dice rolling simulator")

# Pętla for wykona poniższy kod dokładnie 5 razy
for i in range(5):

    # Losujemy liczbę całkowitą od 1 do 6 (jak na kostce)
    # Wynik zapisujemy w zmiennej dice_roll
    dice_roll = random.randint(1, 6)

    # Wyświetlamy wylosowaną liczbę
    # end=" " sprawia, że wyniki są w jednej linii, oddzielone spacjami
    print(dice_roll, end=" ")
