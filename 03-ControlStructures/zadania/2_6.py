# Zadanie 2.6: rozpoznanie liczby dodatniej, ujemnej lub zera.
# f wstawia wartości z {}; :g pokazuje np. 7 zamiast 7.0.

number = float(input('Enter number: '))  # Pobiera liczbę; float pozwala wpisać np. 2.5.
if number > 0:  # Sprawdza, czy liczba jest większa od zera.
    print(f'Number {number:g} is positive')  # Pokazuje, że liczba jest dodatnia.
elif number < 0:  # Sprawdza, czy liczba jest mniejsza od zera.
    print(f'Number {number:g} is negative')  # Pokazuje, że liczba jest ujemna.
else:  # Wybiera tę część, gdy liczba nie jest ani dodatnia, ani ujemna.
    print('Number is 0')  # Pokazuje informację o zerze.
