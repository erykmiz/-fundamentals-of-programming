# Zadanie 6.14: Sprawdzamy, czy osoba ma co najmniej dwa z trzech kont.
# and wymaga obu kont w parze; or oznacza, że wystarczy jedna taka para.

facebook = True  # Zapisuje True, czyli osoba ma Facebooka.
twitter = False  # Zapisuje False, czyli osoba nie ma Twittera.
instagram = True  # Zapisuje True, czyli osoba ma Instagram.
if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):  # Sprawdza trzy możliwe pary kont.
    print('You are a good influencer!')  # Potwierdza spełnienie warunku z ćwiczenia.
else:  # Obsługuje przypadek najwyżej jednego konta.
    print('You need at least two accounts.')  # Informuje, że potrzeba co najmniej dwóch kont.
