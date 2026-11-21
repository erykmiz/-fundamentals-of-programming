# Zadanie 4.8. Zapisujemy tę samą godzinę w formacie 24- lub 12-godzinnym.
# Reguły formatowania liczb opisuje dokumentacja Pythona.
# https://docs.python.org/3/library/string.html#format-specification-mini-language

def time_string(hours, minutes, time_format):  # Przyjmuje godzinę, minutę i wybrany format.
    if time_format == '24':  # Sprawdza, czy wybrano zapis 24-godzinny.
        return f'{hours:02d}:{minutes:02d}'  # :02d uzupełnia godzinę i minutę zerem do dwóch cyfr.

    if time_format == '12':  # Sprawdza, czy wybrano zapis 12-godzinny.
        period = 'am' if hours < 12 else 'pm'  # Ustawia am przed południem, od południa ustawia pm.
        clock_hour = hours % 12  # Zamienia godziny 12–23 na odpowiadający im zakres 0–11.
        if clock_hour == 0:  # Wykrywa północ lub południe po obliczeniu reszty.
            clock_hour = 12  # W zapisie 12-godzinnym wyświetla 12 zamiast zera.
        return f'{clock_hour}:{minutes:02d}{period}'  # Uzupełnia minutę zerem i dodaje am albo pm.

    raise ValueError('Use format 24 or 12.')  # Zgłasza format spoza dwóch dostępnych opcji.


if __name__ == '__main__':  # Uruchamia przykłady po otwarciu pliku jako programu.
    print(time_string(15, 38, '24'))  # Oczekiwany wynik to 15:38.
    print(time_string(8, 3, '24'))  # Oczekiwany wynik to 08:03.
    print(time_string(0, 5, '24'))  # Oczekiwany wynik to 00:05.
    print(time_string(11, 15, '12'))  # Oczekiwany wynik to 11:15am.
    print(time_string(0, 7, '12'))  # Oczekiwany wynik to 12:07am.
    print(time_string(7, 30, '12'))  # Oczekiwany wynik to 7:30am.
    print(time_string(12, 46, '12'))  # Oczekiwany wynik to 12:46pm.
    print(time_string(13, 10, '12'))  # Oczekiwany wynik to 1:10pm.
    print(time_string(19, 2, '12'))  # Oczekiwany wynik to 7:02pm.
