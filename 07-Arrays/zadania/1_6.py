# Zadanie 1.6. Zwracamy angielską nazwę dnia tygodnia na podstawie jego numeru.

def weekday(n):  # Przyjmuje numer dnia od 1 dla poniedziałku do 7 dla niedzieli.
    if not 1 <= n <= 7:  # Sprawdza, czy dzień ma numer spoza dozwolonego zakresu.
        raise ValueError('Day number must be between 1 and 7.')  # Zgłasza błąd dla numeru spoza tygodnia.
    weekdays = [  # Zapisuje nazwy dni w kolejności od poniedziałku.
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',  # Umieszcza dni od pierwszego do czwartego.
        'Friday', 'Saturday', 'Sunday',  # Uzupełnia listę o piątek, sobotę i niedzielę.
    ]  # Kończy listę siedmiu nazw.
    return weekdays[n - 1]  # Odejmuje 1 od numeru dnia, ponieważ lista ma indeksy od zera.


if __name__ == '__main__':  # Wypisuje przykłady przy bezpośrednim uruchomieniu pliku.
    for day in (1, 4, 7):  # Sprawdza kolejno trzy numery podane w poleceniu.
        print(f'Day {day}: {weekday(day)}')  # Wstawia numer i nazwę dnia do wyświetlanego napisu.
