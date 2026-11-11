# Zadanie 6.7: numery Unicode kolejnych liter imienia.
name = "John"  # Zapisuje przykładowe imię; możesz zastąpić je własnym.
for letter in name:  # Powtarza następną linię dla każdej litery imienia, po kolei.
    print(f"The letter {letter} has a code {ord(letter)}")  # Wyświetla aktualną literę i jej numer Unicode.
