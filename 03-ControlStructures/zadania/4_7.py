# Zadanie 4.7: dodajemy parzyste liczby od 1 do 10.
# % oznacza resztę z dzielenia; continue pomija resztę bieżącego powtórzenia.

total = 0  # Zaczyna sumowanie od zera.
for i in range(1, 11):  # Bierze kolejne liczby od 1 do 10.
    if i % 2 != 0:  # Sprawdza, czy liczba jest nieparzysta.
        continue  # Pomija dodawanie tej nieparzystej liczby.
    total += i  # Dodaje liczbę parzystą do sumy.
print(f"Sum of even numbers in the range <1,10> is {total}")  # Wstawia total w {} i pokazuje sumę 30.
