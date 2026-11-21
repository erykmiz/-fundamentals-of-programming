# Zadania 5.4 i 5.5. Funkcje rysują figury tym samym domyślnym żółwiem.

import math  # Udostępnia funkcję pierwiastka potrzebną do obliczenia przeciwprostokątnej.
import turtle  # Udostępnia domyślnego żółwia, którym rysujemy figury.


def draw_square(length):  # Przyjmuje długość każdego boku kwadratu.
    pen = turtle.getturtle()  # Pobiera żółwia z aktualną pozycją i kierunkiem.
    for _ in range(4):  # Powtarza rysowanie boku i obrót cztery razy.
        pen.forward(length)  # Rysuje bok kwadratu o podanej długości.
        pen.right(90)  # Obraca żółwia w prawo o kąt prosty przed następnym bokiem.


def draw_trangle(length):  # Przyjmuje długość dwóch równych boków. Nazwa funkcji pochodzi z polecenia.
    pen = turtle.getturtle()  # Pobiera domyślnego żółwia ustawionego przez program.
    pen.forward(length)  # Rysuje pierwszy z równych boków.
    pen.left(90)  # Ustawia żółwia pod kątem prostym względem pierwszego boku.
    pen.forward(length)  # Rysuje drugi bok tej samej długości.
    pen.left(135)  # Kieruje żółwia od końca drugiego boku do punktu startu.
    pen.forward(length * math.sqrt(2))  # Rysuje przeciwprostokątną wyliczoną z twierdzenia Pitagorasa.
    pen.left(135)  # Przywraca kierunek, w którym żółw zaczynał rysowanie.


def draw_rectangle(lenght_a, lenght_b):  # Przyjmuje długości dwóch sąsiednich boków prostokąta.
    pen = turtle.getturtle()  # Pobiera tego samego żółwia wraz z jego pozycją.
    for _ in range(2):  # Rysuje po dwie pary sąsiednich boków.
        pen.forward(lenght_a)  # Rysuje bok o długości a.
        pen.right(90)  # Obraca się o kąt prosty przed bokiem b.
        pen.forward(lenght_b)  # Rysuje bok o długości b.
        pen.right(90)  # Obraca się o kąt prosty przed kolejnym bokiem.
