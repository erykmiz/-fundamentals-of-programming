# Zadanie 2.3. Podliczamy wydatki miesięczne według kategorii i tygodni.

monthly_expenses = [  # Każdy wiersz to wydatki tygodnia na żywność, transport i opłaty.
    [200, 50, 100],  # Wydatki z pierwszego tygodnia.
    [180, 60, 110],  # Wydatki z drugiego tygodnia.
    [220, 55, 105],  # Wydatki z trzeciego tygodnia.
    [210, 65, 95],  # Wydatki z czwartego tygodnia.
]  # Zamyka listę wydatków.
categories = ['Food', 'Transport', 'Utilities']  # Ustala nazwy kategorii w kolejności kolumn.
category_totals = [0] * len(categories)  # Przygotowuje osobną sumę dla każdej kategorii.
week_totals = []  # Przygotowuje listę, do której trafi suma każdego tygodnia.
month_total = 0  # Ustawia początkową sumę miesięczną.

for week in monthly_expenses:  # Pobiera kolejno dane z każdego tygodnia.
    week_total = 0  # Rozpoczyna zliczanie wydatków nowego tygodnia.
    for index, cost in enumerate(week):  # Pobiera koszt i indeks odpowiadającej mu kategorii.
        category_totals[index] += cost  # Dodaje koszt do sumy danej kategorii.
        week_total += cost  # Dodaje ten sam koszt do sumy bieżącego tygodnia.
    week_totals.append(week_total)  # Zapisuje ukończoną sumę tygodniową na liście.
    month_total += week_total  # Powiększa sumę miesiąca o wydatki tygodnia.

print('MONTHLY EXPENSES')  # Wyświetla tytuł zestawienia.
print('----------------')  # Oddziela tytuł od danych.
for index, category in enumerate(categories):  # Pobiera indeks i nazwę kolejnej kategorii.
    print(f'{category}: {category_totals[index]}')  # Wyświetla sumę przypisaną do kategorii.
for number, total in enumerate(week_totals, start=1):  # Numeruje tygodnie od 1 i odczytuje ich sumy.
    print(f'Week {number}: {total}')  # Wyświetla numer tygodnia i jego wydatki.
print('---------------')  # Oddziela podsumowanie od danych tygodniowych.
print('TOTAL:', month_total)  # Wyświetla całkowite wydatki miesiąca.
