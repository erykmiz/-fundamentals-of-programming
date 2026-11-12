# Zadanie 4.6: dodajemy liczby od 5 do 10.
# += dodaje do obecnej wartości; f wstawia wartości w miejsca {}.

total = 0  # Zaczyna sumowanie od zera.
for i in range(5, 11):  # Bierze liczby 5, 6, 7, 8, 9 i 10, bez 11.
    total += i  # Dodaje i do total; to samo co total = total + i.
print(f"Sum is {total}")  # Pokazuje sumę, czyli 45.
