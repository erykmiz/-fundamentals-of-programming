# Zadanie 3.27. Rysujemy wykres funkcji f(x) = x² - 3 dla x od -100 do 100.
# Bibliotekę Matplotlib można doinstalować poleceniem python -m pip install matplotlib.

import matplotlib.pyplot as plt  # Wczytuje narzędzia do rysowania wykresów pod skrótem plt.

if __name__ == '__main__':  # Rysuje wykres po bezpośrednim uruchomieniu pliku.
    x_values = []  # Przygotowuje listę wartości na osi poziomej.
    y_values = []  # Przygotowuje listę wartości funkcji na osi pionowej.
    for x in range(-100, 101):  # Wybiera całkowite współrzędne x od -100 do 100 włącznie.
        x_values.append(x)  # Dodaje bieżącą współrzędną x do listy.
        y_values.append(x ** 2 - 3)  # Podnosi x do kwadratu, odejmuje 3 i zapisuje wynik.
    plt.plot(x_values, y_values)  # Łączy kolejne pary wartości x i y w wykres paraboli.
    plt.title('f(x) = x² - 3')  # Podaje wzór funkcji w tytule.
    plt.xlabel('x')  # Podpisuje oś poziomą.
    plt.ylabel('f(x)')  # Podpisuje oś wartości funkcji.
    plt.grid(True)  # Włącza siatkę, która ułatwia odczyt wartości.
    plt.show()  # Otwiera okno z wykresem.
