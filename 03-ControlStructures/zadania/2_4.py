# Zadanie 2.4: prosty kalkulator czterech działań.
number1 = float(input('Enter first number: '))  # Pobiera pierwszą liczbę; float pozwala wpisać część dziesiętną po kropce.
number2 = float(input('Enter second number: '))  # Pobiera drugą liczbę.
operator = input('Enter operator (+, -, *, /): ').strip()  # Pobiera symbol działania i usuwa zbędne skrajne spacje.
result = None  # Przyjmuje brak wyniku do chwili wykonania poprawnego działania.
if operator == '+':  # Sprawdza, czy użytkownik wybrał dodawanie.
    result = number1 + number2  # Oblicza sumę dwóch liczb.
elif operator == '-':  # Sprawdza, czy wybrano odejmowanie.
    result = number1 - number2  # Odejmuje drugą liczbę od pierwszej.
elif operator == '*':  # Sprawdza, czy wybrano mnożenie.
    result = number1 * number2  # Oblicza iloczyn dwóch liczb.
elif operator == '/':  # Sprawdza, czy wybrano dzielenie.
    if number2 != 0:  # Upewnia się, że dzielnik nie jest zerem.
        result = number1 / number2  # Dzieli pierwszą liczbę przez drugą.
    else:  # Obsługuje próbę dzielenia przez zero.
        print('Cannot divide by zero')  # Wyświetla wyjaśnienie zamiast przerywać program błędem.
else:  # Obsługuje symbole inne niż cztery dostępne działania.
    print('Incorrect operator')  # Informuje o nierozpoznanym działaniu.
if result is not None:  # Wyświetla wynik tylko wtedy, gdy udało się wykonać działanie.
    print(f'{number1:g} {operator} {number2:g} = {result:g}')  # Pokazuje całe działanie; g pomija zbędne końcowe zera.
