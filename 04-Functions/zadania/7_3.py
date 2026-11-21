# Zadanie 7.3. Wyświetlamy nazwę miesiąca na podstawie jego numeru.

from months import month  # Importuje funkcję month z pliku months.py.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim włączeniu programu.
    for number in (7, 9):  # Sprawdza lipiec z polecenia i wrzesień z przykładu.
        print(f'The name of month {number} is {month(number)}')  # Pokazuje numer i nazwę zwróconą przez funkcję.
