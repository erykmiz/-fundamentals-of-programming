# Zadanie 7.2: hasło musi zawierać co najmniej 8 znaków.
# Przykłady: university i peter123 -> True; seven i anna333 -> False.

password = input('Enter password: ')  # Wczytuje hasło jako tekst wpisany z klawiatury.
password_ok = len(password) >= 8  # Liczy znaki funkcją len() i sprawdza, czy jest ich przynajmniej 8.
print(f'Password length is valid: {password_ok}')  # Wyświetla wynik sprawdzenia długości hasła.
