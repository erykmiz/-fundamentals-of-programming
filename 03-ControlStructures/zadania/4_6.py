# Zadanie 4.6: suma liczb całkowitych od 5 do 10 włącznie.
total = 0  # Przygotowuje zmienną przechowującą sumę; na początku niczego jeszcze nie dodano.
for i in range(5, 11):  # Pobiera liczby 5, 6, 7, 8, 9 i 10; górna granica 11 nie należy do zakresu.
    total += i  # Dodaje aktualną liczbę do sumy; to skrót zapisu total = total + i.
print(f"Sum is {total}")  # Wyświetla obliczoną sumę: 45.
