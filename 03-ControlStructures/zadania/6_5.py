# Zadanie 6.5: opis temperatury według progów z ćwiczenia.

temperature = float(input('Enter temperature in degrees Celsius: '))  # Pobiera temperaturę jako liczbę; część dziesiętną wpisz po kropce.
if temperature > 35:  # Sprawdza temperaturę powyżej 35 stopni.
    print('It is extremely hot')  # Pokazuje opis dla temperatury powyżej 35.
elif temperature > 30:  # Po wykluczeniu wyższego progu sprawdza temperaturę powyżej 30.
    print('It is hot')  # Pokazuje opis dla temperatury ponad 30 do 35 włącznie.
elif temperature >= 15:  # Sprawdza temperaturę od 15 do 30 włącznie.
    print('It is warm')  # Pokazuje opis cieplejszej temperatury.
elif temperature >= 0:  # Sprawdza temperaturę od 0 włącznie do mniej niż 15.
    print('It is cold')  # Pokazuje opis chłodnej temperatury.
else:  # Pozostaje temperatura poniżej zera.
    print('Warning, frost')  # Pokazuje ostrzeżenie o mrozie.
