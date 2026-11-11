# Zadanie 6.7: grupa wiekowa według granic z polecenia.
age = int(input('Enter your age: '))  # Pobiera wiek w pełnych latach.
if age < 0:  # Sprawdza, czy wpisano niepoprawny ujemny wiek.
    print('Incorrect age')  # Informuje o niepoprawnej wartości.
elif age < 13:  # Po wykluczeniu wieku ujemnego sprawdza wiek poniżej 13 lat.
    print('Child')  # Wyświetla grupę dzieci.
elif age <= 19:  # Sprawdza wiek od 13 do 19 lat włącznie.
    print('Teen')  # Wyświetla grupę nastolatków.
elif age <= 64:  # Sprawdza wiek od 20 do 64 lat włącznie.
    print('Adult')  # Wyświetla grupę dorosłych.
else:  # Pozostaje wiek 65 lat lub więcej.
    print('Senior')  # Wyświetla grupę seniorów.
