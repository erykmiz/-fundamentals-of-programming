# Zadanie 6.9: uproszczone rozpoznanie imienia zakończonego literą a.
# Stosujemy regułę z ćwiczenia; sama końcówka nie rozpoznaje poprawnie wszystkich imion.
name = input('Enter name: ').strip()  # Pobiera imię i usuwa spacje z jego początku i końca.
if name.lower().endswith('a'):  # Sprawdza końcówkę po zamianie na małe litery; działa także dla pustego tekstu.
    print(f'{name} -- Polish female name')  # Wyświetla imię tylko wtedy, gdy spełnia warunek z zadania.
