# Zadanie 7.4. Liczymy wystąpienia litery „e” w zdaniu.

from letters import count_letter  # Importuje funkcję z pliku letters.py.


if __name__ == '__main__':  # Uruchamia przykład przy bezpośrednim włączeniu pliku.
    text = 'You never get a second chance to make a first impression'  # Zapisuje tekst podany w zadaniu.
    letter = 'e'  # Wskazuje literę, którą liczymy.
    result = count_letter(text, letter)  # Przekazuje tekst i literę do funkcji oraz zapisuje wynik.
    print(text)  # Pokazuje analizowane zdanie.
    print(f"The number of letter '{letter}': {result}")  # Wyświetla szukaną literę i liczbę jej wystąpień.
