# Zadanie 6.7: grupa wiekowa według granic z polecenia.

age = int(input('Enter your age: '))  # Pobiera wiek w pełnych latach.
if age < 0:  # Odrzuca ujemny wiek.
    print('Incorrect age')  # Pokazuje informację o błędnej wartości.
elif age < 13:  # Po wykluczeniu wartości ujemnych sprawdza wiek 0-12.
    print('Child')  # Pokazuje grupę dzieci.
elif age <= 19:  # Sprawdza pozostały wiek 13-19.
    print('Teen')  # Pokazuje grupę nastolatków.
elif age <= 64:  # Sprawdza pozostały wiek 20-64.
    print('Adult')  # Pokazuje grupę dorosłych.
else:  # Pozostaje wiek co najmniej 65 lat.
    print('Senior')  # Pokazuje grupę seniorów.
