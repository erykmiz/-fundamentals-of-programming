# Zadanie 6.17: zamiana czasu z formatu 24-godzinnego na 12-godzinny.
time_24 = input('Enter time (24-hour format): ')  # Pobiera czas jako tekst, np. 16:32.
if len(time_24) == 5 and time_24.isascii() and time_24[2] == ':' and time_24[0:2].isdigit() and time_24[3:5].isdigit():  # Wymaga dwóch zwykłych cyfr, dwukropka i dwóch zwykłych cyfr.
    hour = int(time_24[0:2])  # Zamienia dwie pierwsze cyfry na numer godziny.
    minute = int(time_24[3:5])  # Zamienia dwie ostatnie cyfry na numer minuty.
    if 0 <= hour <= 23 and 0 <= minute <= 59:  # Wymaga istniejącej godziny i minuty.
        hour_12 = hour % 12  # Oblicza godzinę w cyklu 12-godzinnym, na razie z zerem zamiast 12.
        if hour_12 == 0:  # Rozpoznaje północ albo południe.
            hour_12 = 12  # Zastępuje godzinę 0 godziną 12 zgodnie z formatem 12-godzinnym.
        if hour < 12:  # Sprawdza, czy czas jest przed południem.
            suffix = 'am'  # Ustawia oznaczenie czasu przed południem.
        else:  # Obsługuje południe i godziny popołudniowe.
            suffix = 'pm'  # Ustawia oznaczenie czasu po południu.
        print(f'Time in 12-hour format: {hour_12}:{minute:02d}{suffix}')  # Wyświetla godzinę i minutę zawsze zapisaną dwiema cyframi.
    else:  # Obsługuje liczbę godzin lub minut poza dozwolonym zakresem.
        print('Incorrect time')  # Informuje, że taki czas nie istnieje.
else:  # Obsługuje tekst zapisany w innym układzie niż hh:mm.
    print('Incorrect time; use hh:mm')  # Przypomina wymagany format wpisywania czasu.
