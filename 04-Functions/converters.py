# Zadanie 5.2. Funkcje zamieniające jednostki długości.


def m_to_cm(n):  # Przyjmuje długość w metrach.
    return n * 100  # Zwraca centymetry, bo jeden metr ma 100 centymetrów.


def cm_to_m(n):  # Przyjmuje długość w centymetrach.
    return n / 100  # Zwraca metry przez podzielenie liczby centymetrów przez 100.


def cm_to_inches(n):  # Przyjmuje długość w centymetrach.
    return n / 2.54  # Dzieli długość przez 2.54, bo jeden cal ma 2.54 centymetra.


def feet_inches_to_cm(feet, inches):  # Przyjmuje osobno liczbę stóp i liczbę cali.
    total_inches = feet * 12 + inches  # Przelicza stopy na cale i dodaje pozostałe cale.
    return total_inches * 2.54  # Przelicza łączną liczbę cali na centymetry.


if __name__ == '__main__':  # Pokazuje przykłady po uruchomieniu tego modułu jako programu.
    print(f'2m = {m_to_cm(2)}cm')  # Wyświetla długość dwóch metrów w centymetrach.
    print(f'532cm = {cm_to_m(532)}m')  # Wyświetla długość 532 centymetrów w metrach.
