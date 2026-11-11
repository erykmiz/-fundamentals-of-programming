# Zadanie 7.1: sprawdzenie warunku wieku podanego w ćwiczeniu.
# To uproszczony warunek z zadania, a nie sprawdzenie rzeczywistych przepisów podatkowych.
# Przykłady: 38 -> False, 27 -> False, 26 -> True, 22 -> True, 18 -> True.

age = int(input('Enter age: '))  # Wczytuje wiek i zamienia wpisany tekst na liczbę całkowitą.
no_tax = age <= 26  # Sprawdza, czy wiek jest mniejszy lub równy 26, zgodnie z treścią zadania.
print(f'Exemption from paying taxes: {no_tax}')  # Wyświetla True, gdy warunek jest spełniony, lub False w przeciwnym razie.
