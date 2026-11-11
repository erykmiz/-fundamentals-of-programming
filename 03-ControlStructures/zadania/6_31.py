# Zadanie 6.31: dwadzieścia losowych liczb całkowitych z przedziału od 5 do 10.
import random  # Udostępnia funkcję randint() służącą do losowania liczb całkowitych.
for index in range(20):  # Wykonuje losowanie i wyświetlenie liczby dokładnie dwadzieścia razy.
    number = random.randint(5, 10)  # Losuje liczbę od 5 do 10, włącznie z obiema granicami.
    print(number, end=' ')  # Wyświetla wylosowaną liczbę ze spacją zamiast nowej linii.
print()  # Kończy linię po wyświetleniu dwudziestu wyników.
