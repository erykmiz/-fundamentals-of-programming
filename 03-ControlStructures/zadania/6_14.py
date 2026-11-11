# Zadanie 6.14: sprawdzenie, czy osoba ma co najmniej dwa z trzech kont.
facebook = True  # Wartość True oznacza, że osoba ma konto na Facebooku.
twitter = False  # Wartość False oznacza, że osoba nie ma konta na Twitterze.
instagram = True  # Wartość True oznacza, że osoba ma konto na Instagramie.
if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):  # Sprawdza każdą parę kont; wystarczy, że istnieje jedna pełna para.
    print('You are a good influencer!')  # Wyświetla komunikat, gdy warunek z ćwiczenia jest spełniony.
else:  # Wykonuje tę część, gdy osoba ma najwyżej jedno konto.
    print('You need at least two accounts.')  # Informuje, że do spełnienia warunku brakuje kont.
