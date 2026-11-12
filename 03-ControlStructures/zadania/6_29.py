# Zadanie 6.29: Szukamy N pierwszych liczb pierwszych.
# Liczba pierwsza ma tylko dwa dodatnie dzielniki: 1 i samą siebie.
# Wystarczy sprawdzać do pierwiastka; dalej powtarzałyby się pary, np. 2 * 6 i 6 * 2.

n = int(input('How many prime numbers should be printed? '))  # Pobiera liczbę szukanych wyników N.
if n < 1:  # Sprawdza, czy N jest mniejsze od 1.
    print('Enter a positive number of primes.')  # Prosi o dodatnią liczbę wyników.
else:  # Rozpoczyna szukanie dla poprawnego N.
    found = 0  # Zaczyna liczenie znalezionych liczb od zera.
    candidate = 2  # Zaczyna sprawdzanie kandydatów od liczby 2.
    print('Prime numbers:', end=' ')  # Pokazuje nagłówek bez przejścia do nowej linii.
    while found < n:  # Szuka, dopóki znalezionych liczb jest mniej niż N.
        is_prime = True  # Zakłada, że kandydat jest pierwszy, dopóki nie znajdzie dzielnika.
        divisor = 2  # Zaczyna sprawdzanie dzielników od 2.
        while divisor * divisor <= candidate:  # Sprawdza dzielniki najwyżej do pierwiastka z kandydata.
            if candidate % divisor == 0:  # Sprawdza, czy dzielnik dzieli kandydata bez reszty.
                is_prime = False  # Zapamiętuje, że kandydat nie jest liczbą pierwszą.
                break  # Kończy tylko wewnętrzną pętlę sprawdzania dzielników.
            divisor += 1  # Przechodzi do następnego dzielnika.
        if is_prime:  # Sprawdza, czy kandydat pozostał uznany za pierwszy.
            print(candidate, end=' ')  # Pokazuje znalezioną liczbę pierwszą i spację.
            found += 1  # Zwiększa liczbę znalezionych wyników o 1.
        candidate += 1  # Przechodzi do następnego kandydata.
    print()  # Kończy wiersz po wszystkich wynikach.
