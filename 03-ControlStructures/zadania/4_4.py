# Zadanie 4.4: dodanie spacji między znakami nazwy uczelni.
university = "Krakow University of Economics"  # Zapisuje nazwę uczelni podaną w zadaniu.
university_expanded = ""  # Przygotowuje pusty tekst, do którego będziemy dopisywać znaki.
for char in university:  # Pobiera po kolei każdy znak, również spacje obecne już w nazwie.
    university_expanded = university_expanded + char + " "  # Dopisuje aktualny znak i dodatkową spację.
print(university)  # Wyświetla oryginalną nazwę uczelni.
print(university_expanded.rstrip())  # Wyświetla rozszerzoną nazwę, usuwając zbędną spację na samym końcu.
