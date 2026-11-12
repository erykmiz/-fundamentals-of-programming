# Zadanie 6.15: Sprawdzamy 13 cyfr EAN i osobno początek 590.
# Sprawdzamy format bez cyfry kontrolnej; 590 stosujemy według ćwiczenia, nie jako gwarancję kraju.
# isdigit() sprawdza cyfry, isascii() ogranicza je tu do 0–9; [0:3] bierze pozycje 0, 1, 2.

article_number = input('Enter EAN-13 article number: ')  # Pobiera numer jako tekst, aby zachować początkowe zera.
if len(article_number) == 13 and article_number.isascii() and article_number.isdigit():  # Wymaga jednocześnie długości 13 i zwykłych cyfr 0–9.
    print('Article number is correct')  # Potwierdza poprawny format numeru.
    if article_number[0:3] == '590':  # Sprawdza, czy pierwsze trzy cyfry to 590.
        print('Article manufactured in Poland')  # Pokazuje komunikat przypisany 590 w ćwiczeniu.
else:  # Obsługuje błędną długość lub znaki inne niż cyfry.
    print('Incorrect article number')  # Pokazuje informację o błędnym numerze.
