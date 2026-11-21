# Moduł do zadania 7.3. Zamieniamy numer miesiąca na angielską nazwę.


def month(n):  # Przyjmuje numer miesiąca liczony od 1.
    if not 1 <= n <= 12:  # Sprawdza, czy numer wypada poza zakresem od 1 do 12.
        raise ValueError('Month number must be between 1 and 12')  # Zgłasza błąd dla numeru spoza zakresu.

    names = (  # Tworzy krotkę z nazwami miesięcy w kolejności kalendarzowej.
        'January', 'February', 'March',  # Miesiące od 1 do 3.
        'April', 'May', 'June',  # Miesiące od 4 do 6.
        'July', 'August', 'September',  # Miesiące od 7 do 9.
        'October', 'November', 'December',  # Miesiące od 10 do 12.
    )  # Zamyka krotkę dwunastu nazw.
    return names[n - 1]  # Odejmuje 1, bo pierwszy element krotki ma indeks 0.
