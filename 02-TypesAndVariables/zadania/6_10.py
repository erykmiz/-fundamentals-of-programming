# Zadanie 6.10: sprawdzamy długość tytułu filmu, zmieniamy wielkość liter i szukamy słów.
# Operacje na tekście zwracają wyniki; nie zmieniają tu wartości movie.

movie = "The Lord of the Rings: The Return of the King"  # Zapamiętuje cały tytuł, razem ze spacjami i dwukropkiem.

print("Number of characters:", len(movie))  # Liczy wszystkie znaki tytułu, również spacje i dwukropek; wynik to 45.
print("Uppercase:", movie.upper())  # Tworzy i pokazuje wersję tytułu z samymi wielkimi literami.
print("Lowercase:", movie.lower())  # Tworzy i pokazuje wersję tytułu z samymi małymi literami.
print("Number of e letters:", movie.count("e"))  # Liczy wystąpienia dokładnie małej litery e; w tym tytule jest ich 5.
print("Position of Lord:", movie.find("Lord"))  # Szuka pierwszego Lord i oddaje indeks jego litery L, czyli 4.
print("Position of dragon:", movie.find("dragon"))  # Oddaje -1, bo tekstu dragon nie ma w tytule.
