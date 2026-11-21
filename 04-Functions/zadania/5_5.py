# Zadanie 5.5. Rysujemy po dwa kwadraty, trójkąty równoramienne i prostokąty.

import turtle  # Udostępnia okno i żółwia do rysowania.
import figures  # Wczytuje funkcje rysujące poszczególne figury.


def move_to(pen, x, y):  # Przenosi żółwia do punktu podanego współrzędnymi x i y.
    pen.penup()  # Podnosi pisak, żeby ruch nie zostawił śladu.
    pen.goto(x, y)  # Ustawia pozycję żółwia w nowym miejscu.
    pen.pendown()  # Opuszcza pisak, aby następny ruch rysował.


def main():  # Przygotowuje okno i rysuje figury rozmieszczone w dwóch rzędach.
    window = turtle.Screen()  # Tworzy okno do rysowania figur.
    window.setup(600, 440)  # Ustawia szerokość i wysokość okna w pikselach.
    window.bgcolor('lightgreen')  # Ustawia jasnozielone tło.
    pen = turtle.getturtle()  # Pobiera domyślnego żółwia używanego przez moduł figures.
    pen.speed(5)  # Ustawia prędkość rysowania.

    move_to(pen, -230, 115)  # Ustawia początek pierwszego kwadratu po lewej u góry.
    figures.draw_square(70)  # Rysuje pierwszy kwadrat o boku 70.
    move_to(pen, -230, -65)  # Ustawia początek drugiego kwadratu po lewej na dole.
    figures.draw_square(90)  # Rysuje drugi kwadrat o boku 90.

    move_to(pen, -55, 45)  # Ustawia początek pierwszego trójkąta w górnym rzędzie.
    figures.draw_trangle(70)  # Rysuje pierwszy trójkąt o dwóch bokach długości 70.
    move_to(pen, -55, -150)  # Ustawia początek drugiego trójkąta w dolnym rzędzie.
    figures.draw_trangle(85)  # Rysuje drugi trójkąt o dwóch bokach długości 85.

    move_to(pen, 115, 115)  # Ustawia początek pierwszego prostokąta po prawej u góry.
    figures.draw_rectangle(120, 55)  # Rysuje pierwszy prostokąt o bokach 120 i 55.
    move_to(pen, 115, -65)  # Ustawia początek drugiego prostokąta po prawej na dole.
    figures.draw_rectangle(135, 75)  # Rysuje drugi prostokąt o bokach 135 i 75.

    pen.hideturtle()  # Ukrywa kursor żółwia po narysowaniu wszystkich figur.
    window.mainloop()  # Pozostawia rysunek na ekranie do zamknięcia okna.


if __name__ == '__main__':  # Sprawdza, czy użytkownik uruchomił ten plik bezpośrednio.
    main()  # Uruchamia okno z sześcioma figurami.
