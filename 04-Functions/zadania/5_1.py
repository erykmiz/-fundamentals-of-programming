# Zadanie 5.1. Podział programu na moduły.
# Moduł to plik .py, do którego można przenieść funkcje używane w kilku programach.
# Instrukcja import nazwa_modulu ładuje moduł, a kropka pozwala wywołać jego funkcję.
# Materiały z polecenia.
# https://docs.python.org/3/tutorial/modules.html
# https://www.w3schools.com/python/python_modules.asp

import math  # Wczytuje standardowy moduł math z funkcjami matematycznymi.

if __name__ == '__main__':  # Wykonuje przykład po bezpośrednim uruchomieniu tego pliku.
    result = math.sqrt(49)  # Wywołuje funkcję sqrt z modułu math i zapisuje wynik.
    print(result)  # Wyświetla pierwiastek kwadratowy z 49, czyli 7.0.
