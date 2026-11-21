# Zadanie 5.3. Funkcje odczytujące z klawiatury wartości różnych typów.


def input_string(message):  # Przyjmuje komunikat z pytaniem do użytkownika.
    return input(message)  # Wyświetla pytanie i zwraca wpisany tekst.


def input_integer(message):  # Definiuje funkcję do odczytu liczby całkowitej.
    return int(input(message))  # Odczytuje wpisany tekst i zamienia go na typ int.


def input_real(message):  # Definiuje funkcję do odczytu liczby dziesiętnej.
    return float(input(message))  # Zamienia wpisany tekst z kropką dziesiętną na typ float.


def input_boolean(message):  # Definiuje funkcję do odczytu odpowiedzi y albo n.
    while True:  # Powtarza pytanie, dopóki funkcja nie zwróci wyniku.
        answer = input(message).strip().lower()  # Usuwa skrajne spacje i zamienia litery na małe.
        if answer == 'y':  # Rozpoznaje odpowiedź twierdzącą.
            return True  # Kończy funkcję i zwraca prawdę.
        if answer == 'n':  # Rozpoznaje odpowiedź przeczącą.
            return False  # Kończy funkcję i zwraca fałsz.
        print('Please enter y or n.')  # Informuje, jakiej odpowiedzi oczekuje program.
