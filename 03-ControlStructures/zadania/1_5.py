# Zadanie 1.5: zaliczenie testu po uzyskaniu co najmniej 50% poprawnych odpowiedzi.
# Dla 20 zadań wyniki 20, 11 i 10 oznaczają zaliczenie, a 9 i 0 brak zaliczenia.
total_tasks = 20  # Zapisuje całkowitą liczbę zadań w teście.
tasks_ok = int(input('Enter number of correct tasks: '))  # Pobiera liczbę poprawnie rozwiązanych zadań.
test_passed = False  # Przyjmuje początkowo, że test nie został zaliczony.
if tasks_ok >= total_tasks * 0.5:  # Porównuje wynik z połową wszystkich zadań, czyli z 10.
    test_passed = True  # Zapisuje informację o zaliczeniu, gdy próg został osiągnięty.
if test_passed:  # Sprawdza zapisaną wartość logiczną; True oznacza zaliczenie.
    print('Congratulations! You passed the test.')  # Wyświetla potwierdzenie zaliczenia.
else:  # Wybiera tę część, gdy test_passed ma wartość False.
    print('Unfortunately, you failed the test.')  # Wyświetla informację o niezaliczeniu.
