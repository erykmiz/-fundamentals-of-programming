# Zadanie 1.12. Znajdujemy kategorię o największych wydatkach.

categories = ['Food', 'Transport', 'Rent', 'Entertainment']  # Zapisuje nazwy czterech kategorii.
expenses = [500, 150, 1000, 200]  # Zapisuje kwoty w tej samej kolejności co nazwy kategorii.

highest_expense = max(expenses)  # Znajduje największą kwotę wśród wydatków.
index = expenses.index(highest_expense)  # Odczytuje indeks pierwszego wystąpienia tej kwoty.
category = categories[index]  # Pobiera nazwę kategorii zapisaną pod tym samym indeksem.
print(f'Most expensive category: {category} ({highest_expense})')  # Wypisuje kategorię wraz z kwotą.
