# Zadanie 5.4. Główny program rysujący kwadrat.
# Pętla rysująca kolejne boki, umieszczona początkowo w programie głównym,
# znajduje się teraz w oddzielnym module w funkcji draw_square(length).

import turtle  # Udostępnia okno graficzne i domyślnego żółwia.
from figures import draw_square  # Wczytuje funkcję z pliku figures.py.


def main():  # Przygotowuje okno i uruchamia rysowanie.
    window = turtle.Screen()  # Tworzy okno, w którym pojawi się kwadrat.
    window.bgcolor('lightgreen')  # Ustawia jasnozielone tło.
    pen = turtle.getturtle()  # Pobiera domyślnego żółwia używanego również przez draw_square.
    pen.speed(5)  # Ustawia prędkość animacji rysowania.
    draw_square(100)  # Rysuje kwadrat o boku 100 jednostek.
    pen.hideturtle()  # Ukrywa kursor żółwia po narysowaniu kwadratu.
    window.mainloop()  # Utrzymuje otwarte okno do chwili zamknięcia.


if __name__ == '__main__':  # Umożliwia bezpośrednie uruchomienie również pliku draw_figures.py.
    main()  # Przygotowuje okno i rysuje figurę.
