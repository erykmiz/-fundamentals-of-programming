# Zadanie 7.3: sprawdzamy, czy wpisana liczba całkowita jest parzysta.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

number = int(input('Enter number: '))  # Pyta o liczbę i zapisuje ją jako number, np. tekst '24' zamienia na liczbę 24.
even = number % 2 == 0  # Najpierw liczy resztę z dzielenia przez 2, potem sprawdza, czy ta reszta wynosi 0.
print(f'Number is even: {even}')  # Pokazuje True dla liczby parzystej albo False dla nieparzystej.
