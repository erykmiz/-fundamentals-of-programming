# Zadanie 5.6: sumujemy liczby parzyste pętlą while.
# % 2 == 0 oznacza parzystość; += dodaje do obecnej wartości.

N = 10  # Ustawia górną granicę na 10.
sum_even = 0  # Zaczyna sumę od 0.
number = 1  # Zaczyna sprawdzanie od liczby 1.
while number <= N:  # Sprawdza kolejne liczby aż do N włącznie.
    if number % 2 == 0:  # Sprawdza, czy liczba jest parzysta.
        sum_even += number  # Dodaje parzystą liczbę do sumy.
    number += 1  # Przechodzi do następnej liczby.
print(f"The sum of even numbers from 1 to {N} is: {sum_even}")  # Wstawia wartości w {} i pokazuje sumę 30.
