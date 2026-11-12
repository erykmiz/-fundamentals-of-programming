# Zadanie 6.11: Sprawdzamy, czy cena spadła o co najmniej 10%.
# f wstawia wartości z {}; .2f pokazuje 2 miejsca po kropce, a :g np. 30 zamiast 30.0.

current_price = 140  # Zapisuje obecną cenę: 140.
previous_price = 200  # Zapisuje poprzednią cenę: 200.
reduction_percent = (previous_price - current_price) / previous_price * 100  # Liczy spadek ceny: (200 - 140) / 200 * 100 = 30%.
print(f'Current product price: {current_price:.2f}')  # Pokazuje obecną cenę.
print(f'Previous product price: {previous_price:.2f}')  # Pokazuje poprzednią cenę.
if reduction_percent >= 10:  # Sprawdza, czy obniżka wynosi przynajmniej 10%.
    print('Buy the product!!')  # Pokazuje zalecenie kupna z ćwiczenia.
    print(f'Product price reduced by {reduction_percent:g}%')  # Pokazuje procent obniżki, tutaj 30%.
