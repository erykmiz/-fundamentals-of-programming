# Zadanie 2.5. Liczymy miejsca w kinie i sprawdzamy, które z nich są zajęte.

def seats_total(seats):  # Przyjmuje listę rzędów z miejscami.
    total = 0  # Na początku licznik miejsc wynosi zero.
    for row in seats:  # Przegląda kolejne rzędy.
        total += len(row)  # Dodaje liczbę miejsc w bieżącym rzędzie.
    return total  # Zwraca liczbę wszystkich miejsc w kinie.


def seats_available(seats):  # Przyjmuje plan kina do zliczenia wolnych miejsc.
    available = 0  # Ustawia początkową liczbę wolnych miejsc.
    for row in seats:  # Sprawdza każdy rząd planu.
        available += row.count('A')  # Dodaje liczbę miejsc oznaczonych literą A.
    return available  # Zwraca sumę wolnych miejsc we wszystkich rzędach.


def seats_booked(seats):  # Przyjmuje plan kina do zliczenia zajętych miejsc.
    booked = 0  # Ustawia początkową liczbę zajętych miejsc.
    for row in seats:  # Sprawdza każdy rząd planu.
        booked += row.count('B')  # Dodaje liczbę miejsc oznaczonych literą B.
    return booked  # Zwraca sumę zajętych miejsc we wszystkich rzędach.


def seat_status(seats, row, place):  # Przyjmuje plan, numer rzędu i numer miejsca liczone od 1.
    if not 1 <= row <= len(seats):  # Sprawdza, czy wybrany rząd istnieje.
        raise ValueError('Invalid row number')  # Zgłasza błąd, gdy numer rzędu jest poza zakresem.
    selected_row = seats[row - 1]  # Pobiera rząd, zamieniając numer na indeks listy.
    if not 1 <= place <= len(selected_row):  # Sprawdza, czy miejsce istnieje w tym rzędzie.
        raise ValueError('Invalid seat number')  # Zgłasza błąd, gdy numer miejsca jest poza zakresem.
    if selected_row[place - 1] == 'A':  # Odczytuje stan miejsca o podanym numerze.
        return 'available'  # Zwraca informację o wolnym miejscu.
    return 'booked'  # Dla oznaczenia B zwraca informację o rezerwacji.


if __name__ == '__main__':  # Pokazuje dane przykładowe przy bezpośrednim uruchomieniu pliku.
    cinema_seats = [  # Zapisuje plan zawierający pięć rzędów po pięć miejsc.
        ['A', 'A', 'B', 'A', 'A'],  # Stan miejsc w pierwszym rzędzie.
        ['A', 'B', 'B', 'A', 'A'],  # Stan miejsc w drugim rzędzie.
        ['A', 'A', 'A', 'A', 'B'],  # Stan miejsc w trzecim rzędzie.
        ['B', 'A', 'A', 'A', 'A'],  # Stan miejsc w czwartym rzędzie.
        ['A', 'B', 'A', 'A', 'A'],  # Stan miejsc w piątym rzędzie.
    ]  # Zamyka listę rzędów.

    print('CINEMA INFORMATION TABLE')  # Wyświetla nagłówek zestawienia.
    print('Total seats:', seats_total(cinema_seats))  # Wyświetla liczbę wszystkich miejsc.
    print('Seats available:', seats_available(cinema_seats))  # Wyświetla liczbę wolnych miejsc.
    print('Seats booked:', seats_booked(cinema_seats))  # Wyświetla liczbę zajętych miejsc.
    print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))  # Pokazuje stan pierwszego miejsca w pierwszym rzędzie.
    print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))  # Pokazuje stan piątego miejsca w piątym rzędzie.
    print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))  # Pokazuje stan piątego miejsca w trzecim rzędzie.
