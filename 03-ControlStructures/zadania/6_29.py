# Zadanie 6.29: wypisanie N pierwszych liczb pierwszych.
# N oznacza liczbę szukanych wyników; pierwszość sprawdzamy osobno dla każdego kandydata.
n = int(input('How many prime numbers should be printed? '))  # Wczytuje liczbę szukanych liczb pierwszych.
if n < 1:  # Sprawdza, czy zamówiono przynajmniej jeden wynik.
    print('Enter a positive number of primes.')  # Informuje, że N powinno być dodatnie.
else:  # Rozpoczyna szukanie dla dodatniego N.
    found = 0  # Liczy już znalezione liczby pierwsze.
    candidate = 2  # Zaczyna od najmniejszej liczby pierwszej.
    print('Prime numbers:', end=' ')  # Wyświetla nagłówek bez kończenia linii.
    while found < n:  # Szuka kolejnych kandydatów, dopóki nie znajdzie N wyników.
        is_prime = True  # Zakłada, że kandydat jest pierwszy, dopóki nie znajdzie dzielnika.
        divisor = 2  # Zaczyna sprawdzanie od najmniejszego możliwego dzielnika większego od 1.
        while divisor * divisor <= candidate:  # Sprawdza dzielniki do pierwiastka; większy dzielnik miałby już sprawdzony mniejszy odpowiednik.
            if candidate % divisor == 0:  # Sprawdza, czy dzielenie przez dany dzielnik nie pozostawia reszty.
                is_prime = False  # Oznacza kandydata jako liczbę złożoną po znalezieniu dzielnika.
                break  # Kończy sprawdzanie tego kandydata, bo znaleziony dzielnik już wystarcza.
            divisor += 1  # Przechodzi do następnego potencjalnego dzielnika.
        if is_prime:  # Sprawdza, czy nie znaleziono żadnego dzielnika.
            print(candidate, end=' ')  # Wyświetla znalezioną liczbę pierwszą.
            found += 1  # Zwiększa liczbę gotowych wyników o jeden.
        candidate += 1  # Przechodzi do kolejnej liczby, niezależnie od wyniku sprawdzania.
    print()  # Kończy linię po wypisaniu wszystkich znalezionych liczb.
