# Zadanie 2.3: sprawdzenie typów danych funkcją type().
# int to liczba całkowita, float to liczba z częścią ułamkową, str to tekst, bool to prawda lub fałsz.

print(type(50))  # 50 jest liczbą całkowitą, więc otrzymamy <class 'int'>.
print(type(149.17))  # Liczba z kropką dziesiętną ma typ float.
print(type(4 * 7))  # Mnożenie dwóch liczb całkowitych daje 28 typu int.
print(type(4.0 * 7))  # Użycie liczby 4.0 powoduje, że wynik 28.0 ma typ float.
print(type("Krakow University of Economics"))  # Tekst zapisany w cudzysłowie ma typ str.
print(type(True))  # Wartość logiczna True ma typ bool.
print(type(2 > 5))  # Porównanie daje False, a False ma typ bool.
