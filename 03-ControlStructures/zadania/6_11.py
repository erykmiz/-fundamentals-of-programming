# Zadanie 6.11: sprawdzenie, czy cena spadła o co najmniej 10%.
current_price = 140  # Zapisuje obecną cenę produktu z przykładu.
previous_price = 200  # Zapisuje wcześniejszą cenę produktu z przykładu.
reduction_percent = (previous_price - current_price) / previous_price * 100  # Oblicza spadek ceny jako procent poprzedniej ceny.
print(f'Current product price: {current_price:.2f}')  # Wyświetla obecną cenę z dwoma miejscami po kropce.
print(f'Previous product price: {previous_price:.2f}')  # Wyświetla poprzednią cenę w tym samym formacie.
if reduction_percent >= 10:  # Sprawdza, czy spadek ceny wynosi co najmniej 10%.
    print('Buy the product!!')  # Wyświetla komunikat wymagany w ćwiczeniu.
    print(f'Product price reduced by {reduction_percent:g}%')  # Pokazuje obliczony spadek ceny; g usuwa zbędne końcowe zera.
