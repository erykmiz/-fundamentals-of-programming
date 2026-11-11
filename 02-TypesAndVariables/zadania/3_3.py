# Zadanie 3.3: zamieniamy miejscami wartości dwóch zmiennych: x ma dostać 34, a y ma dostać 7.
# z przechowuje stare x, żeby nie zgubić jego wartości podczas zamiany.

x = 7  # Zapisuje początkowe x = 7.
y = 34  # Zapisuje początkowe y = 34.
z = 0  # Przygotowuje pomocniczą zmienną z.
print("Przed zamianą: x =", x, "y =", y)  # Pokazuje początkowe wartości x = 7 i y = 34.
z = x  # Zapamiętuje stare x, czyli 7, w z.
x = y  # Wpisuje 34 do x; teraz x i y mają 34, a z nadal 7.
y = z  # Wpisuje zachowane 7 do y; zamiana jest gotowa.
print("Po zamianie: x =", x, "y =", y)  # Pokazuje końcowe wartości: x = 34 oraz y = 7.
