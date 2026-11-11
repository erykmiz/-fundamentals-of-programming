# Zadanie 2.2: opis rozmiaru ubrania.
size = input('Enter size symbol: ').strip().upper()  # Pobiera rozmiar, usuwa skrajne spacje i zamienia litery na wielkie.
if size == 'S':  # Sprawdza, czy wpisano mały rozmiar S.
    print('S: Small size')  # Wyświetla opis rozmiaru S.
elif size == 'M':  # Sprawdza rozmiar M, jeśli wcześniejszy warunek był fałszywy.
    print('M: Medium size')  # Wyświetla opis średniego rozmiaru.
elif size == 'L':  # Sprawdza, czy podano rozmiar L.
    print('L: Large size')  # Wyświetla opis dużego rozmiaru.
elif size == 'XL':  # Sprawdza, czy podano rozmiar XL.
    print('XL: Extra large size')  # Wyświetla opis bardzo dużego rozmiaru.
else:  # Obsługuje wszystkie symbole inne niż S, M, L i XL.
    print('Incorrect symbol')  # Informuje, że rozmiar nie jest rozpoznawany.
