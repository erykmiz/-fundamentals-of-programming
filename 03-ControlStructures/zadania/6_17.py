# Zadanie 6.17: Zamieniamy czas 24-godzinny na 12-godzinny.
# [0:2] bierze znaki 0 i 1; isascii() ogranicza znaki do ASCII, a isdigit() sprawdza cyfry w wycinkach.
# % 12 daje godzinę w cyklu 12-godzinnym; :02d zapisuje minutę dwiema cyframi, np. 07.

time_24 = input('Enter time (24-hour format): ')  # Pobiera czas jako tekst, np. 16:32.
if len(time_24) == 5 and time_24.isascii() and time_24[2] == ':' and time_24[0:2].isdigit() and time_24[3:5].isdigit():  # Sprawdza układ: dwie cyfry, dwukropek, dwie cyfry.
    hour = int(time_24[0:2])  # Zamienia dwie pierwsze cyfry na godzinę.
    minute = int(time_24[3:5])  # Zamienia dwie ostatnie cyfry na minutę.
    if 0 <= hour <= 23 and 0 <= minute <= 59:  # Sprawdza zakres godziny 0–23 i minuty 0–59.
        hour_12 = hour % 12  # Liczy resztę z dzielenia godziny przez 12.
        if hour_12 == 0:  # Sprawdza, czy otrzymano 0, czyli północ lub południe.
            hour_12 = 12  # Zastępuje 0 godziną 12 w nowym zapisie.
        if hour < 12:  # Sprawdza, czy czas jest przed południem.
            suffix = 'am'  # Ustawia oznaczenie am.
        else:  # Obsługuje godziny od południa.
            suffix = 'pm'  # Ustawia oznaczenie pm.
        print(f'Time in 12-hour format: {hour_12}:{minute:02d}{suffix}')  # Pokazuje wynik, np. 4:32pm.
    else:  # Obsługuje godzinę lub minutę poza zakresem.
        print('Incorrect time')  # Pokazuje informację o błędnym czasie.
else:  # Obsługuje zapis niezgodny z hh:mm.
    print('Incorrect time; use hh:mm')  # Przypomina poprawny format wpisywania czasu.
