# Zadanie 2.6: rozpoznanie liczby dodatniej, ujemnej lub zera.
number = float(input('Enter number: '))  # Pobiera liczbę, która może mieć część dziesiętną.
if number > 0:  # Sprawdza, czy liczba jest większa od zera.
    print(f'Number {number:g} is positive')  # Wyświetla informację o liczbie dodatniej.
elif number < 0:  # Sprawdza, czy liczba jest mniejsza od zera.
    print(f'Number {number:g} is negative')  # Wyświetla informację o liczbie ujemnej.
else:  # Wybiera tę część, gdy liczba nie jest ani dodatnia, ani ujemna.
    print('Number is 0')  # Informuje, że wpisano zero.
