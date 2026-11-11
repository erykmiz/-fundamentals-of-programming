# Zadanie 5.5: liczymy kwotę obniżki oraz cenę po rabacie.
# f wstawia wartości z {}; :.2f pokazuje 2 miejsca po kropce, a :g pomija np. końcówkę .0.

price = float(input("Enter price: "))  # Pobiera cenę przed rabatem, np. 24.72, i zapisuje ją w price.
discount = float(input("Enter discount %: "))  # Pobiera procent rabatu; wpisz np. 15, bez znaku %.
reduction = price * discount / 100  # Liczy kwotę obniżki; dla przykładu 24.72 * 15 / 100 = 3.708.
discounted_price = price - reduction  # Odejmuje obniżkę od ceny; w przykładzie 24.72 - 3.708 = 21.012.

print(f"Price before discount: {price:.2f}")  # Pokazuje cenę początkową z dwiema cyframi po kropce.
print(f"Discount: {discount:g}%")  # Pokazuje procent rabatu i dopisuje znak %, np. 15%.
print(f"Price with discount: {discounted_price:.2f}")  # Pokazuje cenę po obniżce; w przykładzie 21.01.
print(f"Reduction: {reduction:.2f}")  # Pokazuje kwotę obniżki; w przykładzie 3.71.
