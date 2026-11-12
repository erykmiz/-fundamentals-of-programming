# Zadanie 6.3: liczba świecących żarówek zależna od dwóch włączników.
# Oba if sprawdzamy niezależnie, więc można włączyć łącznie 3 żarówki.

light_switch1 = False  # False wyłącza pierwszy włącznik; True włączyłoby jedną żarówkę.
light_switch2 = False  # False wyłącza drugi włącznik; True włączyłoby dwie żarówki.
bulbs_on = 0  # Zaczyna liczenie od zera.
if light_switch1:  # Sprawdza pierwszy włącznik.
    bulbs_on += 1  # += 1 dodaje jedną świecącą żarówkę.
if light_switch2:  # Niezależnie sprawdza drugi włącznik.
    bulbs_on += 2  # Dodaje dwie świecące żarówki.
print(f'Bulbs on: {bulbs_on}')  # f wstawia wynik do {} i pokazuje liczbę żarówek.
