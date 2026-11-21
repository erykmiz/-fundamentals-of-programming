# Zadanie 7.6. Wyświetlamy zamaskowany przykładowy numer karty.

from card_mask import hide  # Importuje funkcję hide z pliku card_mask.py.


if __name__ == '__main__':  # Uruchamia przykład przy bezpośrednim włączeniu pliku.
    card_number = '5290312400019022'  # Zapisuje przykładowy numer jako tekst, aby można było pobrać jego fragmenty.
    print(hide(card_number))  # Wyświetla numer po zastąpieniu środkowych cyfr gwiazdkami.
