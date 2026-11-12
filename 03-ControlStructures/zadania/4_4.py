# Zadanie 4.4: dodajemy spacje między znakami nazwy uczelni.
# + łączy teksty, a rstrip() usuwa białe znaki z końca tekstu.

university = "Krakow University of Economics"  # Zapisuje pełną nazwę uczelni.
university_expanded = ""  # Przygotowuje pusty tekst na wynik.
for char in university:  # Bierze kolejny znak nazwy, także spację.
    university_expanded = university_expanded + char + " "  # Dopisuje znak i dodatkową spację do wyniku.
print(university)  # Pokazuje oryginalną nazwę.
print(university_expanded.rstrip())  # Pokazuje wynik bez zbędnej spacji na końcu.
