# Zadanie 4.7. Literujemy imię za pomocą alfabetu fonetycznego ICAO.
# Pełne rozwiązanie z komentarzem do każdej linii znajduje się w pliku icao.py w folderze 04-Functions.

from pathlib import Path  # Udostępnia klasę do pracy ze ścieżkami plików.
from runpy import run_path  # Udostępnia funkcję uruchamiającą plik Pythona pod podaną ścieżką.

if __name__ == '__main__':  # Uruchamia program przy otwarciu tego pliku jako skryptu.
    program = Path(__file__).resolve().parent.parent / 'icao.py'  # Szuka icao.py obok folderu zadania.
    run_path(str(program), run_name='__main__')  # Wykonuje icao.py razem z blokiem odczytu imienia.
