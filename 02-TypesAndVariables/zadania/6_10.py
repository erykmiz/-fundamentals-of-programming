# Zadanie 6.10: podstawowe operacje na tytule filmu.
movie = "The Lord of the Rings: The Return of the King"  # Zapisuje tytuł filmu jako tekst.
print("Number of characters:", len(movie))  # Liczy wszystkie znaki tytułu, również spacje i dwukropek.
print("Uppercase:", movie.upper())  # Tworzy i wyświetla wersję tytułu z samymi wielkimi literami.
print("Lowercase:", movie.lower())  # Tworzy i wyświetla wersję tytułu z samymi małymi literami.
print("Number of e letters:", movie.count("e"))  # Liczy wystąpienia małej litery e w oryginalnym tytule.
print("Position of Lord:", movie.find("Lord"))  # Podaje pozycję początku słowa Lord, licząc od 0: 4.
print("Position of dragon:", movie.find("dragon"))  # Zwraca -1, ponieważ słowa dragon nie ma w tytule.
