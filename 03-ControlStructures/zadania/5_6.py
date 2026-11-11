# Zadanie 5.6: zastąpienie pętli for pętlą while przy sumowaniu liczb parzystych.
N = 10  # Zapisuje górną granicę zakresu podaną w przykładowym programie.
sum_even = 0  # Przygotowuje sumę liczb parzystych.
number = 1  # Rozpoczyna sprawdzanie liczb od jedynki.
while number <= N:  # Sprawdza kolejne liczby aż do N włącznie.
    if number % 2 == 0:  # Rozpoznaje liczbę parzystą po zerowej reszcie z dzielenia przez 2.
        sum_even += number  # Dodaje liczbę do sumy tylko wtedy, gdy jest parzysta.
    number += 1  # Przechodzi do następnej liczby, dzięki czemu pętla się zakończy.
print(f"The sum of even numbers from 1 to {N} is: {sum_even}")  # Wyświetla wynik 30 dla zakresu od 1 do 10.
