# Zadanie 5.3. Wczytujemy dane pracownika i pytamy, czy ukryć pensję w podsumowaniu.

import keyboard  # Wczytuje funkcje do pobierania danych z sąsiedniego pliku keyboard.py.


def main():  # Łączy pobieranie danych z wyświetlaniem rekordu pracownika.
    first_name = keyboard.input_string('Enter name: ')  # Wczytuje imię jako tekst.
    last_name = keyboard.input_string('Enter surname: ')  # Wczytuje nazwisko jako tekst.
    age = keyboard.input_integer('Enter age: ')  # Wczytuje wiek jako liczbę całkowitą.
    salary = keyboard.input_real('Enter salary: ')  # Wczytuje pensję jako liczbę dziesiętną.
    is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n): ')  # Zapisuje True, jeśli pensja ma być ukryta.

    print('DATA RECORD')  # Drukuje tytuł podsumowania.
    print('===========')  # Rysuje linię pod tytułem.
    print('Name:', first_name)  # Wyświetla imię pracownika.
    print('Surname:', last_name)  # Wyświetla nazwisko pracownika.
    print('Age:', age)  # Wyświetla wiek pracownika.
    if not is_salary_hidden:  # Odwraca wartość logiczną, żeby wykonać blok po odpowiedzi n.
        print(f'Salary: {salary:.2f}')  # Wyświetla pensję z dwiema cyframi po kropce.


if __name__ == '__main__':  # Sprawdza, czy użytkownik uruchomił ten plik bezpośrednio.
    main()  # Wczytuje dane i pokazuje podsumowanie.
