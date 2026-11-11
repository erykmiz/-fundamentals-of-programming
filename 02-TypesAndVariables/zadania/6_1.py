# Zadanie 6.1: liczba znaków w imieniu, nazwisku i pełnym imieniu z nazwiskiem.
# Anna May to dane przykładowe; możesz wpisać własne.
name = "Anna"  # Zapisuje przykładowe imię jako tekst.
surname = "May"  # Zapisuje przykładowe nazwisko jako tekst.
characters_in_name = len(name)  # Liczy znaki w imieniu: 4.
full_name = name + " " + surname  # Łączy imię i nazwisko z jedną spacją pośrodku.
print(f"Your name has {characters_in_name} characters")  # Wyświetla liczbę znaków w imieniu.
print(f"Your surname has {len(surname)} characters")  # Liczy i wyświetla znaki w nazwisku: 3.
print(f"Your full name has {len(full_name)} characters")  # Liczy także spację; Anna May ma 8 znaków.
