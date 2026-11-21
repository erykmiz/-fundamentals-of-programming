# Zadanie 3.9. Szukamy imienia o największej liczbie znaków.

names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']  # Zapisuje podane imiona.
longest_name = names[0]  # Na początku zapamiętuje pierwsze imię jako najdłuższe.
for name in names[1:]:  # Przegląda pozostałe imiona.
    if len(name) > len(longest_name):  # Porównuje długość imienia z długością dotychczasowego najdłuższego.
        longest_name = name  # Zapamiętuje nowe najdłuższe imię.
print('Names:', *names)  # Wyświetla wszystkie imiona w jednym wierszu.
print('Longest name:', longest_name)  # Wyświetla najdłuższe imię, czyli Celestyna.
