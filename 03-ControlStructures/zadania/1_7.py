# Zadanie 1.7: wynagrodzenie bez premii lub z premią 30%.
# Używamy 30% wymaganych w poleceniu, zamiast przykładowych 15% ze szkieletu kodu.
basic_salary = 5000  # Zapisuje podstawowe wynagrodzenie podane w zadaniu.
total_salary = 0  # Przygotowuje zmienną na całkowite wynagrodzenie.
bonus = 0.30  # Zapisuje 30% jako ułamek dziesiętny 0.30.
is_bonus = input('Does the employee receive a bonus? (Y/N): ').strip().upper() == 'Y'  # Pobiera odpowiedź i sprawdza, czy jest to Y, czyli tak.
if is_bonus:  # Sprawdza, czy pracownik otrzymuje premię.
    total_salary = basic_salary + basic_salary * bonus  # Dodaje do podstawy premię 1500, otrzymując 6500.
else:  # Wybiera tę część, gdy pracownik nie otrzymuje premii.
    total_salary = basic_salary  # Pozostawia samo wynagrodzenie podstawowe 5000.
print(f'Basic salary: {basic_salary:.2f}')  # Wyświetla podstawę z dwoma miejscami po przecinku.
print(f'Bonus included? {is_bonus}')  # Wyświetla True dla premii lub False dla jej braku.
print(f'Total salary: {total_salary:.2f}')  # Wyświetla całkowite wynagrodzenie.
