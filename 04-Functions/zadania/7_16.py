# Zadanie 7.16. Obliczamy n-ty wyraz ciągu Fibonacciego, zaczynając numerację od 1.


def f(n):  # Przyjmuje numer wyrazu.
    if n < 1:  # Sprawdza, czy numer jest mniejszy od 1.
        raise ValueError('The term number must be positive')  # Zgłasza błąd dla numeru spoza przyjętej numeracji.
    current = 0  # Zapisuje pierwszy wyraz ciągu.
    next_value = 1  # Zapisuje drugi wyraz ciągu.
    for step in range(1, n):  # Wykonuje n - 1 przejść od pierwszego wyrazu do n-tego.
        current, next_value = next_value, current + next_value  # Przesuwa parę o jeden wyraz, używając obu starych wartości.
    return current  # Zwraca wyraz, do którego doszliśmy.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim włączeniu pliku.
    print(f(5))  # Pokazuje piąty wyraz ciągu, czyli 3.
    print(f(9))  # Pokazuje dziewiąty wyraz ciągu, czyli 21.
