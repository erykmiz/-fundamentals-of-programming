# Zadanie 5.2. Przykłady wywołania funkcji z modułu converters.

import converters  # Wczytuje funkcje z pliku converters.py w tym samym folderze.


def main():  # Łączy wszystkie przykładowe przeliczenia w jednej funkcji.
    print('### Test converters')  # Wyświetla nagłówek przykładowych wyników.
    print(f'Three meters is {converters.m_to_cm(3)}cm')  # Wyświetla liczbę centymetrów w trzech metrach.
    print(f'250 cm = {converters.cm_to_m(250):g} m')  # Zamienia centymetry na metry. Format :g pomija zbędne zera na końcu.
    print(f'25.4 cm = {converters.cm_to_inches(25.4):g} in')  # Pokazuje wynik zamiany 25.4 centymetra na cale.
    print(f'5 ft 7 in = {converters.feet_inches_to_cm(5, 7):.2f} cm')  # Pokazuje centymetry z dwiema cyframi po kropce.


if __name__ == '__main__':  # Sprawdza, czy użytkownik uruchomił ten plik bezpośrednio.
    main()  # Wywołuje funkcję drukującą przykładowe wyniki.
