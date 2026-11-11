# Zadanie 6.5: opis temperatury według progów z ćwiczenia.
# Przykłady: 33 -> hot; 30 -> warm; 8 i 0 -> cold; -2 -> frost.
temperature = float(input('Enter temperature in degrees Celsius: '))  # Pobiera temperaturę; dopuszcza liczbę dziesiętną wpisaną z kropką.
if temperature > 35:  # Sprawdza najwyższy próg, czyli temperaturę powyżej 35 stopni.
    print('It is extremely hot')  # Wyświetla opis dla temperatury powyżej 35 stopni.
elif temperature > 30:  # Po wykluczeniu wyższego progu sprawdza temperaturę powyżej 30 stopni.
    print('It is hot')  # Wyświetla opis dla temperatury powyżej 30 i najwyżej 35 stopni.
elif temperature >= 15:  # Sprawdza temperaturę od 15 do 30 stopni włącznie.
    print('It is warm')  # Wyświetla opis ciepłej pogody.
elif temperature >= 0:  # Sprawdza temperaturę od 0 włącznie do mniej niż 15 stopni.
    print('It is cold')  # Wyświetla opis chłodnej pogody.
else:  # Pozostają temperatury poniżej 0 stopni.
    print('Warning, frost')  # Wyświetla ostrzeżenie o mrozie.
