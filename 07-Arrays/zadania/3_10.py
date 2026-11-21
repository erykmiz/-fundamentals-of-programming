# Zadanie 3.10. Rysujemy z gwiazdek słupki odpowiadające wartościom z tablicy.

def star(n):  # Przyjmuje liczbę gwiazdek do utworzenia.
    return '*' * n  # Powtarza znak gwiazdki n razy i zwraca powstały napis.


if __name__ == '__main__':  # Uruchamia przykład, gdy plik startuje jako program.
    numbers = [2, 6, 4, 9, 7]  # Zapisuje liczby z polecenia.
    for number in numbers:  # Pobiera kolejno każdą liczbę z tablicy.
        print(f'{number}: {star(number)}')  # Wyświetla liczbę i tyle gwiazdek, ile wskazuje jej wartość.
