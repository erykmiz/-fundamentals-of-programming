# Zadanie 4.7: suma liczb parzystych od 1 do 10.
total = 0  # Przygotowuje sumę, do której będą dodawane tylko liczby parzyste.
for i in range(1, 11):  # Sprawdza wszystkie liczby od 1 do 10 włącznie.
    if i % 2 != 0:  # Rozpoznaje liczbę nieparzystą po reszcie z dzielenia przez 2 różnej od zera.
        continue  # Pomija dalszą część tego powtórzenia pętli, więc liczba nieparzysta nie trafi do sumy.
    total += i  # Dodaje liczbę parzystą do sumy.
print(f"Sum of even numbers in the range <1,10> is {total}")  # Wyświetla wynik 2 + 4 + 6 + 8 + 10, czyli 30.
