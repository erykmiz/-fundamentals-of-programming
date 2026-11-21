# Zadanie 3.26. Rysujemy odcinek od punktu (1, 3) do punktu (8, 10).
# Bibliotekę Matplotlib można doinstalować poleceniem python -m pip install matplotlib.
# Dokumentacja funkcji plot znajduje się pod adresem https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

import matplotlib.pyplot as plt  # Wczytuje narzędzia do rysowania wykresów pod skrótem plt.

if __name__ == '__main__':  # Rysuje wykres po bezpośrednim uruchomieniu pliku.
    x_points = [1, 8]  # Zapisuje współrzędne poziome początku i końca odcinka.
    y_points = [3, 10]  # Zapisuje odpowiadające im współrzędne pionowe.
    plt.plot(x_points, y_points, marker='o')  # Łączy punkty linią i zaznacza końce okręgami.
    plt.xlabel('x')  # Podpisuje oś poziomą.
    plt.ylabel('y')  # Podpisuje oś pionową.
    plt.grid(True)  # Włącza siatkę, która ułatwia odczyt współrzędnych.
    plt.show()  # Otwiera okno z wykresem.
