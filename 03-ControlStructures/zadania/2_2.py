# Zadanie 2.2: opis rozmiaru ubrania.

size = input('Enter size symbol: ').strip().upper()  # Pobiera rozmiar; strip usuwa skrajne spacje, a upper zmienia litery na wielkie.
if size == 'S':  # == porównuje wpisany tekst z S.
    print('S: Small size')  # Pokazuje opis małego rozmiaru S.
elif size == 'M':  # Sprawdza M, jeśli wcześniejszy warunek nie pasował.
    print('M: Medium size')  # Pokazuje opis średniego rozmiaru M.
elif size == 'L':  # Sprawdza rozmiar L.
    print('L: Large size')  # Pokazuje opis dużego rozmiaru L.
elif size == 'XL':  # Sprawdza rozmiar XL.
    print('XL: Extra large size')  # Pokazuje opis bardzo dużego rozmiaru XL.
else:  # Obsługuje wszystkie inne symbole.
    print('Incorrect symbol')  # Pokazuje informację o błędnym symbolu.
