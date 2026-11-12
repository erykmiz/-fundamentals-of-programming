# Zadanie 3.4: przynajmniej jedna liczba nie jest ujemna.
# not x < 0 znaczy, że x nie jest ujemne; or wymaga choć jednej takiej liczby.

x = int(input('Enter first number: '))  # Pobiera pierwszą liczbę całkowitą.
y = int(input('Enter second number: '))  # Pobiera drugą liczbę całkowitą.
if not x < 0 or not y < 0:  # Sprawdza, czy x lub y jest równe 0 albo dodatnie.
    print(f'At least one of the numbers {x} and {y} is not negative')  # Pokazuje, że przynajmniej jedna liczba jest nieujemna.
else:  # Wybiera tę część, gdy obie liczby są ujemne.
    print(f'Both numbers {x} and {y} are negative')  # Pokazuje, że obie liczby są mniejsze od zera.
