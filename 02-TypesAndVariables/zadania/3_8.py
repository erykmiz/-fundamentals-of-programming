# Zadanie 3.8: naprawiamy program, który miał policzyć średnią z czterech ocen: 5, 4, 5 i 3.

math = 5  # Zapisuje ocenę 5 z matematyki; math jest tu zwykłą nazwą oceny, nie importowanym modułem.
art = 4  # Zapisuje ocenę 4 z plastyki pod nazwą art.
music = 5  # Zapisuje ocenę 5 z muzyki pod nazwą music.
history = 3  # Zapisuje liczbę 3; usunięto cudzysłowy z '3', aby była to liczba do dodawania, a nie tekst.
average = (math + art + music + history) / 4  # Liczy (5 + 4 + 5 + 3) / 4 = 17 / 4 = 4.25 i zapisuje średnią.
print("Średnia ocen:", average)  # Pokazuje podpis i liczbę 4.25; poprawiono nazwę average oraz parę cudzysłowów w tekście.
