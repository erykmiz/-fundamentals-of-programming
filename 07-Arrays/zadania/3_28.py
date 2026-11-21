# Zadanie 3.28. Rysujemy wykres sinusa dla kątów od 0 do 360 stopni.
# Bibliotekę Matplotlib można doinstalować poleceniem python -m pip install matplotlib.

import math  # Wczytuje funkcje sinus i zamiany stopni na radiany.
import matplotlib.pyplot as plt  # Wczytuje narzędzia do rysowania wykresów pod skrótem plt.

if __name__ == '__main__':  # Rysuje wykres po bezpośrednim uruchomieniu pliku.
    angles = list(range(361))  # Tworzy listę kątów od 0 do 360 stopni włącznie.
    sine_values = []  # Przygotowuje listę wartości sinusa.
    for angle in angles:  # Przechodzi kolejno przez wszystkie kąty.
        radians = math.radians(angle)  # Zamienia kąt ze stopni na radiany wymagane przez math.sin.
        sine_values.append(math.sin(radians))  # Oblicza sinus i dopisuje go do listy wyników.
    plt.plot(angles, sine_values)  # Łączy punkty wykresu od 0 do 360 stopni.
    plt.title('y = sin(x)')  # Umieszcza wzór funkcji nad wykresem.
    plt.xlabel('x (degrees)')  # Wskazuje, że oś pozioma przedstawia stopnie.
    plt.ylabel('sin(x)')  # Podpisuje oś pionową wartościami sinusa.
    plt.xticks(range(0, 361, 45))  # Rozmieszcza oznaczenia osi poziomej co 45 stopni.
    plt.grid(True)  # Włącza siatkę, która ułatwia odczyt wartości.
    plt.show()  # Otwiera okno z wykresem.
