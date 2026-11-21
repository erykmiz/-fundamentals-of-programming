# Zadanie 1.13. Obliczamy łączną wartość towarów w magazynie.

product_prices = [  # Zapisuje ceny jednostkowe dziesięciu towarów.
    2999.99, 149.99, 499.99, 89.99, 1199.99,  # Dodaje ceny pierwszych pięciu towarów.
    349.99, 189.99, 99.99, 249.99, 999.99,  # Dodaje ceny pozostałych pięciu towarów.
]  # Kończy listę cen.
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]  # Zapisuje ilości towarów w tej samej kolejności.

total = 0  # Ustawia wartość całego magazynu na zero przed dodawaniem.
for index in range(len(product_prices)):  # Przechodzi po kolejnych indeksach towarów.
    price = product_prices[index]  # Odczytuje cenę jednej sztuki bieżącego towaru.
    quantity = product_quantities[index]  # Odczytuje liczbę sztuk towaru o tym samym indeksie.
    total += price * quantity  # Mnoży cenę przez liczbę sztuk i dodaje wynik do sumy.

print(f'Total stock value: {total:.2f}')  # Wyświetla wartość zapasów z dwiema cyframi po kropce.
