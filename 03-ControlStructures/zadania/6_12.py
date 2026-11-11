# Zadanie 6.12: rabat 25% na każdą sztukę ponad pierwsze dwie.
number_of_products = int(input('Number of products purchased: '))  # Wczytuje liczbę kupionych sztuk jako liczbę całkowitą.
product_price = float(input('Product price: '))  # Wczytuje cenę jednej sztuki jako liczbę.
if number_of_products < 0 or product_price < 0:  # Odrzuca ujemną liczbę sztuk lub ujemną cenę.
    print('Number of products and price cannot be negative.')  # Wyjaśnia, dlaczego nie można obliczyć zakupu.
elif number_of_products <= 2:  # Dla maksymalnie dwóch sztuk nie stosuje rabatu.
    amount_to_pay = number_of_products * product_price  # Mnoży liczbę sztuk przez ich pełną cenę.
    print(f'Amount to pay: {amount_to_pay:.2f}')  # Wyświetla kwotę z dwoma miejscami po kropce.
else:  # Wykonuje tę część dla zakupu przynajmniej trzech sztuk.
    amount_to_pay = 2 * product_price + (number_of_products - 2) * product_price * 0.75  # Pierwsze dwie sztuki liczy w pełnej cenie, a pozostałe za 75% ceny.
    print(f'Amount to pay: {amount_to_pay:.2f}')  # Wyświetla kwotę; dla pięciu sztuk po 40 otrzymasz 170.00.
