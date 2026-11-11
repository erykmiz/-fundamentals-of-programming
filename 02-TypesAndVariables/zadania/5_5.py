# Zadanie 5.5: cena produktu po obniżce i wartość obniżki.
# Liczby dziesiętne wpisuj z kropką, np. 24.72.
price = float(input("Enter price: "))  # Pobiera cenę przed obniżką jako liczbę.
discount = float(input("Enter discount %: "))  # Pobiera rabat w procentach, np. 15 oznacza 15%.
reduction = price * discount / 100  # Zamienia procent na część ceny i liczy kwotę obniżki.
discounted_price = price - reduction  # Odejmuje obniżkę od ceny początkowej.
print(f"Price before discount: {price:.2f}")  # Wyświetla cenę początkową z dwoma miejscami po przecinku.
print(f"Discount: {discount:g}%")  # Wyświetla procent rabatu; g usuwa zbędne końcowe zera.
print(f"Price with discount: {discounted_price:.2f}")  # Wyświetla nową cenę; dla 24.72 i 15% będzie to 21.01.
print(f"Reduction: {reduction:.2f}")  # Wyświetla różnicę cen; dla danych z przykładu będzie to 3.71.
