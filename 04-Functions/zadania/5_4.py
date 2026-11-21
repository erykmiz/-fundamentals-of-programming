# Zadanie 5.4. Rysujemy kwadrat za pomocą funkcji z osobnego modułu.
# draw_figures.py uruchamia okno, a figures.py zawiera pętlę rysującą boki kwadratu.

from draw_figures import main  # Pobiera funkcję uruchamiającą program opisany w draw_figures.py.

if __name__ == '__main__':  # Uruchamia rysunek po bezpośrednim starcie tego pliku.
    main()  # Otwiera okno programu i rysuje kwadrat.
