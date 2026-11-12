# Zadanie 6.4: hasło musi mieć przynajmniej 12 znaków.

new_password = input('Enter new password: ')  # Pobiera hasło jako tekst.
if len(new_password) < 12:  # len liczy znaki; sprawdza, czy jest ich mniej niż 12.
    print('Password too short (min. 12 chars)')  # Pokazuje informację o zbyt krótkim haśle.
else:  # Pozostaje hasło mające co najmniej 12 znaków.
    print('Password length is correct')  # Potwierdza poprawną długość hasła.
