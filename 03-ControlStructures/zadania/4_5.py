# Zadanie 4.5: przesuwamy litery o jedną pozycję w alfabecie.
# ord() daje numer znaku w Unicode, a chr() zamienia numer z powrotem na znak.
# Po z wracamy do a, a po Z do A; znaki inne niż litery A-Z i a-z zostają bez zmian.

plain_text = "The early bird catches the worm"  # Zapisuje zdanie do zaszyfrowania.
encrypted_text = ""  # Przygotowuje pusty tekst na wynik.
for char in plain_text:  # Bierze kolejny znak zdania.
    code = ord(char)  # Odczytuje numer Unicode tego znaku.
    if "a" <= char <= "z" or "A" <= char <= "Z":  # Sprawdza, czy znak jest literą A-Z lub a-z.
        if char == "z":  # Sprawdza ostatnią małą literę alfabetu.
            code = ord("a")  # Wybiera numer litery a zamiast znaku po z.
        elif char == "Z":  # Sprawdza ostatnią wielką literę alfabetu.
            code = ord("A")  # Wybiera numer litery A zamiast znaku po Z.
        else:  # Obsługuje pozostałe litery.
            code += 1  # Zwiększa numer o 1, czyli wybiera następną literę.
        encrypted_char = chr(code)  # Zamienia nowy numer na literę.
    else:  # Obsługuje znaki inne niż litery alfabetu angielskiego.
        encrypted_char = char  # Pozostawia taki znak bez zmiany.
    encrypted_text += encrypted_char  # Dopisuje otrzymany znak na koniec wyniku.
print(plain_text)  # Pokazuje pierwotne zdanie.
print(encrypted_text)  # Pokazuje zaszyfrowane zdanie.
