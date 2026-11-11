# Zadanie 1.2: sprawdzamy działania, zapisujemy dane i obliczamy pole trójkąta oraz średnią.
# f wstawia wartości z {}; :.2f pokazuje 2 miejsca po kropce, bez zmiany wartości zmiennej.

print(7 + 4)  # Python dodaje 7 i 4, a print pokazuje wynik 11.
print((30 + 10) / 2)  # Najpierw liczy nawias: 30 + 10 = 40, potem 40 / 2 = 20.0.
print(2 ** 3)  # ** oznacza potęgowanie: 2 ** 3 to 2 * 2 * 2, czyli 8.
print(7 > 5)  # > pyta, czy 7 jest większe od 5; odpowiedź True znaczy „tak, to prawda”.
r = 4  # Zapamiętuję liczbę 4 pod nazwą r; tutaj r oznacza promień koła.
area = 3.14159 * r * r  # * mnoży: pole koła to przybliżenie pi * 4 * 4, czyli 50.26544.
print(area)  # Odczytuje wartość zapamiętaną pod nazwą area i pokazuje 50.26544.
print(round(area, 2))  # Pokazuje 50.27; round(area, 2) bez przypisania nie zmienia area.
first_name = "Mary"  # Zapisuje tekst Mary pod nazwą first_name, czyli „imię”.
last_name = "Brown"  # Zapisuje tekst Brown pod nazwą last_name, czyli „nazwisko”.
full_name = first_name + " " + last_name  # Zapisuje połączony tekst Mary Brown pod nazwą full_name.
print(full_name)  # Pokazuje tekst Mary Brown, który został zapisany w full_name.
print(full_name)  # Pokazuje ten sam tekst ponownie, bo polecenie print jest osobnym punktem zadania.
print(len(full_name))  # len liczy znaki: 4 w Mary + 1 spacja + 5 w Brown = 10; print pokazuje 10.

a = 5  # Zapamiętuje długość podstawy trójkąta: 5.
h = 4  # Zapamiętuje wysokość trójkąta: 4.
triangle_area = a * h / 2  # Liczy pole trójkąta: 5 * 4 / 2 = 20 / 2 = 10.0.
print(triangle_area)  # Pokazuje obliczone pole trójkąta: 10.0.

average = (7 + 12 + 31) / 3  # Dodaje trzy liczby w nawiasie: 50, a potem dzieli przez ich liczbę: 3.
print(f"{average:.2f}")  # Pokazuje średnią 50 / 3 jako 16.67; nie zmienia wartości zapisanej w average.
