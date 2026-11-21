# Zadanie 4.4. Sumujemy cyfry liczby całkowitej. Znak minus pomijamy.

def sum_digits(number):  # Przyjmuje liczbę, której cyfry chcemy zsumować.
    digits = str(abs(number))  # abs pomija znak minus, a str zamienia liczbę na tekst.
    total = 0  # Ustawia początkową sumę przed dodaniem cyfr.
    for digit in digits:  # Pobiera po kolei znaki w zapisie liczby.
        total += int(digit)  # Zamienia bieżący znak na cyfrę i dolicza jej wartość.
    return total  # Zwraca sumę po dodaniu wszystkich cyfr.


if __name__ == '__main__':  # Uruchamia część interaktywną przy starcie pliku.
    any_number = int(input('Enter integer number: '))  # Odczytuje liczbę całkowitą.
    result = sum_digits(any_number)  # Oblicza sumę cyfr wczytanej liczby.
    print(f'The sum of the digits in the number {any_number} is {result}')  # Wyświetla wynik.
