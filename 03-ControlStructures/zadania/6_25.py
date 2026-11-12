# Zadanie 6.25: Powtarzamy każdą cyfrę tyle razy, ile wynosi jej wartość.
# str zamienia liczbę na tekst; tekst * liczba powtarza tekst, np. "3" * 3 daje "333".

for number in range(1, 10):  # Wybiera kolejno liczby od 1 do 9.
    print(str(number) * number)  # Pokazuje cyfrę powtórzoną odpowiednią liczbę razy.
