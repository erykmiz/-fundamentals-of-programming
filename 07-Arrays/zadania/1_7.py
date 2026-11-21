# Zadanie 1.7. Wypisujemy każdy produkt z listy zakupów w osobnym wierszu.

shopping_list = [  # Tworzy listę produktów w podanej kolejności.
    'milk', 'bread', 'eggs', 'butter', 'cheese',  # Zapisuje pierwszych pięć produktów.
    'tomatoes', 'potatoes', 'carrots', 'onions', 'garlic',  # Zapisuje pozostałych pięć produktów.
]  # Kończy listę zakupów.

for item in shopping_list:  # Pobiera kolejno każdy produkt z listy.
    print(item)  # Wypisuje nazwę produktu i przechodzi do nowego wiersza.
