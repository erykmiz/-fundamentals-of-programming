# Zadanie 1.7: wynagrodzenie bez premii lub z premią 30%.
# strip() usuwa skrajne spacje, upper() zmienia litery na wielkie; == porównuje odpowiedź z Y.
# f wstawia wartości z {}; :.2f pokazuje dwa miejsca po kropce.

basic_salary = 5000  # Zapisuje pensję podstawową: 5000.
total_salary = 0  # Przygotowuje miejsce na całe wynagrodzenie.
bonus = 0.30  # 0.30 oznacza premię 30% wymaganą w zadaniu.
is_bonus = input('Does the employee receive a bonus? (Y/N): ').strip().upper() == 'Y'  # Porządkuje odpowiedź i zapisuje True dla Y, a False dla pozostałych odpowiedzi.
if is_bonus:  # Sprawdza, czy pracownik otrzymuje premię.
    total_salary = basic_salary + basic_salary * bonus  # Dodaje 5000 + 5000 * 0.30 = 6500.
else:  # Wybiera tę część, gdy pracownik nie otrzymuje premii.
    total_salary = basic_salary  # Zapisuje samą podstawę, czyli 5000.
print(f'Basic salary: {basic_salary:.2f}')  # Pokazuje pensję podstawową z dwoma miejscami po kropce.
print(f'Bonus included? {is_bonus}')  # Pokazuje True dla premii albo False dla jej braku.
print(f'Total salary: {total_salary:.2f}')  # Pokazuje obliczone całkowite wynagrodzenie.
