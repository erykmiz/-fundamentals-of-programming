# Zadanie 3.4: przynajmniej jedna liczba nie jest ujemna.
x = int(input('Enter first number: '))  # Pobiera pierwszą liczbę całkowitą.
y = int(input('Enter second number: '))  # Pobiera drugą liczbę całkowitą.
if not x < 0 or not y < 0:  # not odwraca sprawdzenie ujemności, a or wymaga przynajmniej jednej liczby równej 0 lub dodatniej.
    print(f'At least one of the numbers {x} and {y} is not negative')  # Potwierdza, że przynajmniej jedna liczba jest nieujemna.
else:  # Wybiera tę część, gdy obie liczby są mniejsze od zera.
    print(f'Both numbers {x} and {y} are negative')  # Informuje, że obie liczby są ujemne.
