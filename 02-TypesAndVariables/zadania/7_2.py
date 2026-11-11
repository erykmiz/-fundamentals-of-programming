# Zadanie 7.2: sprawdzamy, czy hasło ma przynajmniej 8 znaków.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

password = input('Enter password: ')  # Pokazuje pytanie, czeka na wpisanie hasła i zapisuje otrzymany tekst jako password.
password_ok = len(password) >= 8  # >= znaczy „większe lub równe”; zapisuje True dla 8 lub więcej znaków, inaczej False.
print(f'Password length is valid: {password_ok}')  # Wyświetla opis oraz wynik sprawdzenia długości hasła.
