# Zadanie 6.3: liczba świecących żarówek zależna od dwóch włączników.
light_switch1 = False  # Ustawia pierwszy włącznik jako wyłączony; zmień na True, aby zapalić jedną żarówkę.
light_switch2 = False  # Ustawia drugi włącznik jako wyłączony; True zapala dwie pozostałe żarówki.
bulbs_on = 0  # Zaczyna liczenie od zera świecących żarówek.
if light_switch1:  # Sprawdza, czy pierwszy włącznik jest włączony.
    bulbs_on += 1  # Dodaje jedną świecącą żarówkę do wyniku.
if light_switch2:  # Niezależnie od pierwszego sprawdza stan drugiego włącznika.
    bulbs_on += 2  # Dodaje dwie świecące żarówki.
print(f'Bulbs on: {bulbs_on}')  # Wyświetla liczbę zapalonych żarówek, od 0 do 3.
