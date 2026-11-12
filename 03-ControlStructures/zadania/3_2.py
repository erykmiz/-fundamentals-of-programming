# Zadanie 3.2: sprawdzenie przykładowego loginu i hasła z ćwiczenia.

login = 'joe'  # Zapisuje przykładowy poprawny login.
password = 'abcd'  # Zapisuje przykładowe hasło z zadania.
entered_login = input('Login: ')  # Pobiera login wpisany jako tekst.
entered_password = input('Password: ')  # Pobiera hasło wpisane jako tekst.
if login == entered_login and password == entered_password:  # == porównuje, a and wymaga jednocześnie dobrego loginu i hasła.
    print('You are logged in')  # Potwierdza zalogowanie przy obu poprawnych wartościach.
else:  # Obsługuje sytuację, gdy co najmniej jedna wartość jest błędna.
    print('Incorrect login or password!!')  # Pokazuje informację o błędnym loginie lub haśle.
