# Zadanie 6.10: wiek psa przeliczony według uproszczenia z ćwiczenia.
# Przez pierwsze 2 lata dodajemy po 10.5 psiego roku, a za każdy kolejny rok po 4.
dog_age = float(input("Enter the dog's age in human years: "))  # Pobiera wiek psa w latach, także z częścią dziesiętną.
dog_years = None  # Przyjmuje brak wyniku do chwili sprawdzenia wieku.
if dog_age < 0:  # Sprawdza, czy podano niepoprawny ujemny wiek.
    print('Incorrect age')  # Informuje o błędnej wartości.
elif dog_age <= 2:  # Sprawdza, czy pies ma najwyżej dwa lata.
    dog_years = dog_age * 10.5  # Mnoży każdy z pierwszych dwóch lat przez 10.5.
else:  # Wybiera tę część dla wieku powyżej dwóch lat.
    dog_years = 2 * 10.5 + (dog_age - 2) * 4  # Dodaje 21 za pierwsze dwa lata i po 4 za każdy następny.
if dog_years is not None:  # Wyświetla wynik wyłącznie dla poprawnego wieku.
    print(f"The dog's age in dog's years is {dog_years:g} years.")  # Pokazuje przeliczony wiek; dla 15 lat otrzymuje 73.
