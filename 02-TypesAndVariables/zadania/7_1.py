# Zadanie 7.1: sprawdzamy, czy podany wiek spełnia warunek z ćwiczenia.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

age = int(input('Enter age: '))  # Pyta o wiek, zamienia odpowiedź na liczbę i zapamiętuje ją pod nazwą age.
no_tax = age <= 26  # <= znaczy „mniejsze lub równe”; dla 26 zapisuje True, dla 27 zapisuje False.
print(f'Exemption from paying taxes: {no_tax}')  # Wstawia obliczone True lub False do zdania i wyświetla całe zdanie.
