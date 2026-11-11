# Zadanie 6.4: hasło musi mieć przynajmniej 12 znaków.
new_password = input('Enter new password: ')  # Pobiera hasło jako tekst.
if len(new_password) < 12:  # Liczy znaki i sprawdza, czy jest ich mniej niż wymagane 12.
    print('Password too short (min. 12 chars)')  # Informuje, że hasło nie spełnia warunku długości.
else:  # Wybiera tę część dla długości co najmniej 12 znaków.
    print('Password length is correct')  # Potwierdza spełnienie warunku z zadania.
