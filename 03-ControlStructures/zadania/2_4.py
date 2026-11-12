# Zadanie 2.4: prosty kalkulator czterech działań.
# = zapisuje wynik, == porównuje; None oznacza brak wyniku.
# f wstawia wartości z {}; :g daje zwięzły zapis liczb.

number1 = float(input('Enter first number: '))  # Pobiera pierwszą liczbę; float dopuszcza część po kropce.
number2 = float(input('Enter second number: '))  # Pobiera drugą liczbę.
operator = input('Enter operator (+, -, *, /): ').strip()  # Pobiera znak działania i usuwa skrajne spacje.
result = None  # None oznacza brak obliczonego wyniku; to nie jest zero.
if operator == '+':  # Sprawdza znak dodawania.
    result = number1 + number2  # Dodaje obie liczby i zapisuje wynik.
elif operator == '-':  # Sprawdza znak odejmowania.
    result = number1 - number2  # Odejmuje drugą liczbę od pierwszej.
elif operator == '*':  # Sprawdza znak mnożenia.
    result = number1 * number2  # Mnoży obie liczby.
elif operator == '/':  # Sprawdza znak dzielenia.
    if number2 != 0:  # != oznacza różne; dzielnik musi być różny od zera.
        result = number1 / number2  # Dzieli pierwszą liczbę przez drugą.
    else:  # Wybiera tę część przy dzieleniu przez zero.
        print('Cannot divide by zero')  # Pokazuje informację, że nie można dzielić przez zero.
else:  # Obsługuje inne, niedozwolone znaki działania.
    print('Incorrect operator')  # Pokazuje informację o błędnym operatorze.
if result is not None:  # Sprawdza, czy wynik istnieje; liczba 0 też jest poprawnym wynikiem.
    print(f'{number1:g} {operator} {number2:g} = {result:g}')  # Pokazuje obie liczby, znak działania i wynik.
