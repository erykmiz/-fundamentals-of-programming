# Zadanie 4.5: szyfr Cezara przesuwający litery alfabetu angielskiego o jedną pozycję.
# Po z wracamy do a, a po Z do A; spacje i znaki inne niż litery A-Z oraz a-z pozostają bez zmian.
plain_text = "The early bird catches the worm"  # Zapisuje przykładowe zdanie przeznaczone do zaszyfrowania.
encrypted_text = ""  # Przygotowuje pusty tekst na zaszyfrowany wynik.
for char in plain_text:  # Pobiera kolejno każdy znak oryginalnego zdania.
    code = ord(char)  # Zamienia aktualny znak na jego numer Unicode.
    if "a" <= char <= "z" or "A" <= char <= "Z":  # Sprawdza, czy znak jest małą lub wielką literą alfabetu angielskiego.
        if char == "z":  # Osobno obsługuje ostatnią małą literę alfabetu.
            code = ord("a")  # Wraca na początek alfabetu, czyli do litery a.
        elif char == "Z":  # Sprawdza, czy trzeba zawinąć ostatnią wielką literę alfabetu.
            code = ord("A")  # Wraca na początek alfabetu wielkich liter.
        else:  # Obsługuje pozostałe litery, które nie wymagają powrotu na początek alfabetu.
            code += 1  # Zwiększa numer znaku o jeden, wybierając następną literę.
        encrypted_char = chr(code)  # Zamienia obliczony numer z powrotem na literę.
    else:  # Obsługuje spacje, cyfry i inne znaki spoza podanego alfabetu.
        encrypted_char = char  # Zachowuje taki znak bez zmiany.
    encrypted_text += encrypted_char  # Dopisuje otrzymany znak na koniec zaszyfrowanego tekstu.
print(plain_text)  # Wyświetla oryginalne zdanie.
print(encrypted_text)  # Wyświetla zaszyfrowane zdanie: Uif fbsmz cjse dbudift uif xpsn.
