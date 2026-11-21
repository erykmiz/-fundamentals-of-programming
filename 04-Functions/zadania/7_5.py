# Zadanie 7.5. Sprawdzamy, czy 7 należy do przedziału domkniętego <2,15>.

from number_range import in_range  # Importuje funkcję sprawdzającą przedział z pliku number_range.py.


if __name__ == '__main__':  # Uruchamia przykład przy bezpośrednim włączeniu pliku.
    number = 7  # Ustawia sprawdzaną liczbę.
    lower = 2  # Ustawia lewą granicę przedziału.
    upper = 15  # Ustawia prawą granicę przedziału.
    answer = 'yes' if in_range(number, lower, upper) else 'no'  # Zamienia True na „yes”, a False na „no”.
    print(f'A number: {number}')  # Pokazuje liczbę używaną w przykładzie.
    print(f'Number {number} in the range <{lower},{upper}>: {answer}')  # Pokazuje granice oraz odpowiedź.
