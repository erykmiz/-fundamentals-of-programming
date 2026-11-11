# Zadanie 2.3: sprawdzamy, jaki rodzaj wartości daje każde wyrażenie.

print(type(50))  # 50 nie ma części po kropce i jest liczbą całkowitą; type daje int, a print go pokazuje.
print(type(149.17))  # Liczba 149.17 jest zapisana z kropką dziesiętną, więc jej typ to float.
print(type(4 * 7))  # Najpierw liczy 4 * 7 = 28; obie liczby są całkowite, więc wynik ma typ int.
print(type(4.0 * 7))  # Najpierw liczy 4.0 * 7 = 28.0; obecność 4.0 sprawia, że wynik ma typ float.
print(type("Krakow University of Economics"))  # Cudzysłowy oznaczają tekst, dlatego type zwraca str.
print(type(True))  # True oznacza prawdę i jest wartością logiczną; jej typ to bool.
print(type(2 > 5))  # Najpierw pyta, czy 2 jest większe od 5; odpowiedź False jest typu bool.
