# Zadanie 6.10: wiek psa przeliczony według uproszczenia z ćwiczenia.
# f wstawia wynik z {}; :g daje zwięzły zapis, np. 73 zamiast 73.0.

dog_age = float(input("Enter the dog's age in human years: "))  # Pobiera wiek psa; float pozwala wpisać np. 1.5.
dog_years = None  # None oznacza brak obliczonego wyniku.
if dog_age < 0:  # Odrzuca ujemny wiek.
    print('Incorrect age')  # Pokazuje informację o błędnej wartości.
elif dog_age <= 2:  # Sprawdza pierwsze dwa lata życia.
    dog_years = dog_age * 10.5  # Liczy po 10.5 psiego roku za każdy z pierwszych dwóch lat.
else:  # Obsługuje wiek powyżej dwóch lat.
    dog_years = 2 * 10.5 + (dog_age - 2) * 4  # Dodaje 21 za pierwsze dwa lata i po 4 za każdy następny.
if dog_years is not None:  # Pokazuje wynik tylko wtedy, gdy został obliczony.
    print(f"The dog's age in dog's years is {dog_years:g} years.")  # Pokazuje przeliczony wiek; np. 15 lat daje 73.
