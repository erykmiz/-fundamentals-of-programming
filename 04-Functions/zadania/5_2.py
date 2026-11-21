# Zadanie 5.2. Sprawdzamy przeliczanie jednostek długości.
# Funkcje oraz przykłady są opisane w converters.py i test_converters.py w folderze 04-Functions.

import sys  # Udostępnia listę katalogów, w których Python szuka modułów.
from pathlib import Path  # Udostępnia obiekt do pracy ze ścieżkami do plików.

if __name__ == '__main__':  # Uruchamia przykłady tylko po bezpośrednim starcie tego pliku.
    chapter_folder = Path(__file__).resolve().parent.parent  # Przechodzi od tego pliku przez zadania do 04-Functions.
    sys.path.insert(0, str(chapter_folder))  # Dodaje 04-Functions na początku listy przeszukiwanych katalogów.
    from test_converters import main  # Pobiera funkcję z przykładami z pliku test_converters.py.
    main()  # Uruchamia przykłady z oryginalnego pliku ćwiczenia.
