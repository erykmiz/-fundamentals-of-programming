# Zadanie 1.5: zaliczenie testu po uzyskaniu co najmniej 50% poprawnych odpowiedzi.

total_tasks = 20  # Zapisuje liczbę wszystkich zadań: 20.
tasks_ok = int(input('Enter number of correct tasks: '))  # Pobiera liczbę poprawnych odpowiedzi jako liczbę całkowitą.
test_passed = False  # Na początku zapisuje False, czyli brak zaliczenia.
if tasks_ok >= total_tasks * 0.5:  # Sprawdza próg 20 * 0.5 = 10 poprawnych odpowiedzi.
    test_passed = True  # Zapisuje True, czyli zaliczenie testu.
if test_passed:  # Wykonuje poniższą linię, jeśli test_passed ma wartość True.
    print('Congratulations! You passed the test.')  # Pokazuje wiadomość o zaliczeniu.
else:  # Wybiera tę część, gdy test_passed ma wartość False.
    print('Unfortunately, you failed the test.')  # Pokazuje wiadomość o niezaliczeniu.
