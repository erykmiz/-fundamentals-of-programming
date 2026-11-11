# Zadanie 6.1: liczymy znaki w imieniu, nazwisku oraz w obu połączonych spacją.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

name = "Anna"  # Zapamiętuje tekst Anna jako przykładowe imię.
surname = "May"  # Zapamiętuje tekst May jako przykładowe nazwisko.
characters_in_name = len(name)  # len() liczy znaki tekstu Anna, więc zapisuje liczbę 4.
full_name = name + " " + surname  # Plusy łączą teksty: Anna, spację i May, tworząc Anna May.

print(f"Your name has {characters_in_name} characters")  # Pokazuje liczbę znaków imienia: 4.
print(f"Your surname has {len(surname)} characters")  # Liczy 3 znaki nazwiska May i pokazuje wynik.
print(f"Your full name has {len(full_name)} characters")  # Liczy 4 + 1 + 3 = 8 znaków tekstu Anna May, w tym spację.
