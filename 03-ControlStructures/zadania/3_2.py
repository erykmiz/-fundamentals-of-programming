# Zadanie 3.2: sprawdzenie przykładowego loginu i hasła z ćwiczenia.
login = 'joe'  # Zapisuje poprawny przykładowy login podany w zadaniu.
password = 'abcd'  # Zapisuje przykładowe hasło używane wyłącznie w tym ćwiczeniu.
entered_login = input('Login: ')  # Pobiera login wpisany przez użytkownika.
entered_password = input('Password: ')  # Pobiera hasło wpisane przez użytkownika.
if login == entered_login and password == entered_password:  # Wymaga jednocześnie poprawnego loginu i poprawnego hasła.
    print('You are logged in')  # Wyświetla potwierdzenie, gdy obie wartości są poprawne.
else:  # Wybiera tę część, gdy co najmniej jedna wpisana wartość jest niepoprawna.
    print('Incorrect login or password!!')  # Informuje o błędnych danych.
