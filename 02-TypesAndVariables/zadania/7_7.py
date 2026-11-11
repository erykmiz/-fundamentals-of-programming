# Zadanie 7.7: pięć losowań liczby całkowitej z przedziału od 5 do 10.
# Pętla powtarza losowanie pięć razy, aby od razu wykonać polecenie z ćwiczenia.

import random  # Udostępnia funkcje służące do losowania liczb.
for i in range(5):  # Powtarza wcięte instrukcje 5 razy; i przyjmuje kolejno wartości od 0 do 4.
    random_number = random.randint(5, 10)  # Losuje liczbę całkowitą od 5 do 10, włącznie z obiema granicami.
    print(random_number)  # Wyświetla wylosowaną liczbę w osobnym wierszu.
