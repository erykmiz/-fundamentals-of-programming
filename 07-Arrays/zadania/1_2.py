# Zadanie 1.2. Materiał o tworzeniu i modyfikowaniu list.
# https://www.w3schools.com/python/python_lists.asp

numbers = [2, 3, 7]  # Tworzy listę z trzema liczbami w zapisanej kolejności.
numbers[1] = 5  # Zastępuje drugi element liczbą 5, ponieważ indeksy zaczynają się od zera.
numbers.append(9)  # Dodaje liczbę 9 na końcu listy.
numbers.remove(2)  # Usuwa pierwsze wystąpienie liczby 2 z listy.
print(numbers)  # Pokazuje listę po zmianach, czyli [5, 7, 9].
