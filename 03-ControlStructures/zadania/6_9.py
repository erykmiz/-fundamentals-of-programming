# Zadanie 6.9: uproszczone rozpoznanie imienia zakończonego literą a.
# Sprawdzamy uproszczoną regułę końcówki imienia podaną w ćwiczeniu.

name = input('Enter name: ').strip()  # Pobiera imię; strip usuwa spacje z początku i końca.
if name.lower().endswith('a'):  # lower zmienia litery na małe, a endswith sprawdza końcówkę a.
    print(f'{name} -- Polish female name')  # f wstawia imię w {} i pokazuje wiadomość po spełnieniu warunku.
