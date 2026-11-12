# Zadanie 6.12: Rabat 25% na każdą sztukę ponad pierwsze dwie.
# 0.75 oznacza 75% ceny, czyli cenę po obniżce o 25%; .2f pokazuje 2 miejsca po kropce.

number_of_products = int(input('Number of products purchased: '))  # Pobiera liczbę sztuk i zamienia tekst na liczbę całkowitą.
product_price = float(input('Product price: '))  # Pobiera cenę sztuki; float pozwala wpisać np. 40.50.
if number_of_products < 0 or product_price < 0:  # Sprawdza, czy liczba sztuk lub cena jest ujemna.
    print('Number of products and price cannot be negative.')  # Pokazuje informację o błędnych danych.
elif number_of_products <= 2:  # Obsługuje zakup najwyżej dwóch sztuk.
    amount_to_pay = number_of_products * product_price  # Liczy wszystkie sztuki po pełnej cenie.
    print(f'Amount to pay: {amount_to_pay:.2f}')  # Pokazuje kwotę do zapłaty.
else:  # Obsługuje zakup co najmniej trzech sztuk.
    amount_to_pay = 2 * product_price + (number_of_products - 2) * product_price * 0.75  # Liczy 2 sztuki po pełnej cenie, a resztę za 75% ceny.
    print(f'Amount to pay: {amount_to_pay:.2f}')  # Pokazuje wynik; dla 5 sztuk po 40 jest to 170.00.
