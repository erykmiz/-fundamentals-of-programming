# Zadanie 1.2: obliczenia, zmienne, pole trójkąta i średnia.
# W trybie interaktywnym sam zapis wyrażenia pokazuje wynik; w pliku używamy print().

print(7 + 4)  # Dodaje 7 i 4 oraz wyświetla wynik 11.
print((30 + 10) / 2)  # Najpierw dodaje liczby w nawiasie, potem dzieli 40 przez 2; wynik: 20.0.
print(2 ** 3)  # Oblicza 2 do potęgi 3, czyli 2 * 2 * 2; wynik: 8.
print(7 > 5)  # Sprawdza, czy 7 jest większe od 5; wynik True oznacza prawdę.
r = 4  # Zapisuje promień koła równy 4 w zmiennej r.
area = 3.14159 * r * r  # Oblicza pole koła ze wzoru pi * promień * promień.
print(area)  # Wyświetla obliczone pole koła: 50.26544.
print(round(area, 2))  # Zaokrągla pole do dwóch miejsc po przecinku i wyświetla 50.27.
first_name = "Mary"  # Zapisuje przykładowe imię jako tekst.
last_name = "Brown"  # Zapisuje przykładowe nazwisko jako tekst.
full_name = first_name + " " + last_name  # Łączy imię i nazwisko, wstawiając pomiędzy nimi jedną spację.
print(full_name)  # Pokazuje wartość zmiennej full_name: Mary Brown.
print(full_name)  # Wykonuje polecenie print(full_name) wymienione osobno w treści zadania.
print(len(full_name))  # Liczy znaki w imieniu i nazwisku razem ze spacją; wynik: 10.

a = 5  # Zapisuje długość podstawy trójkąta podaną w zadaniu.
h = 4  # Zapisuje wysokość trójkąta podaną w zadaniu.
triangle_area = a * h / 2  # Oblicza pole trójkąta ze wzoru podstawa * wysokość / 2.
print(triangle_area)  # Wyświetla pole trójkąta: 10.0.

average = (7 + 12 + 31) / 3  # Dodaje trzy liczby i dzieli sumę przez ich liczbę.
print(f"{average:.2f}")  # Wyświetla średnią z dokładnie dwoma miejscami po przecinku: 16.67.
