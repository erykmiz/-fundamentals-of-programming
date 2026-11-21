# Zadanie 4.6. Zwracamy angielską nazwę dnia tygodnia na podstawie numeru od 1 do 7.

def day_name(day_number):  # Przyjmuje numer dnia, licząc od poniedziałku.
    if day_number == 1:  # Sprawdza, czy wybrano pierwszy dzień tygodnia.
        return 'Monday'  # Zwraca nazwę poniedziałku.
    elif day_number == 2:  # Sprawdza, czy numer oznacza wtorek.
        return 'Tuesday'  # Zwraca nazwę wtorku.
    elif day_number == 3:  # Sprawdza, czy numer oznacza środę.
        return 'Wednesday'  # Zwraca nazwę środy.
    elif day_number == 4:  # Sprawdza, czy numer oznacza czwartek.
        return 'Thursday'  # Zwraca nazwę czwartku.
    elif day_number == 5:  # Sprawdza, czy numer oznacza piątek.
        return 'Friday'  # Zwraca nazwę piątku.
    elif day_number == 6:  # Sprawdza, czy numer oznacza sobotę.
        return 'Saturday'  # Zwraca nazwę soboty.
    elif day_number == 7:  # Sprawdza, czy numer oznacza niedzielę.
        return 'Sunday'  # Zwraca nazwę niedzieli.
    return ''  # Zwraca pusty tekst dla numeru spoza tygodnia.


if __name__ == '__main__':  # Wykonuje trzy przykłady przy bezpośrednim uruchomieniu pliku.
    print('The name of day 5 in the week is', day_name(5))  # Wyświetla nazwę piątku.
    print('The name of day 3 in the week is', day_name(3))  # Wyświetla nazwę środy.
    print('The name of day 7 in the week is', day_name(7))  # Wyświetla nazwę niedzieli.
