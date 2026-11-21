# Zadanie 3.21. Zliczamy liczby większe od progu wpisanego z klawiatury.

numbers = [1.5, -2.1, 4.75, 2.0, 7.25, 0.5]  # Przygotowuje przykładową listę liczb rzeczywistych.
threshold = float(input('Enter a number: '))  # Zamienia odpowiedź użytkownika na liczbę rzeczywistą.
count = 0  # Zaczyna z licznikiem równym zero.
for number in numbers:  # Sprawdza kolejno każdą liczbę na liście.
    if number > threshold:  # Porównuje liczbę z wpisanym progiem.
        count += 1  # Zwiększa licznik po znalezieniu większej wartości.
print('Array:', numbers)  # Wypisuje analizowaną listę.
print('Numbers greater than the given value:', count)  # Pokazuje, ile liczb przekracza próg.
