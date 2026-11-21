# Zadanie 3.17. Wyświetlamy krotkę w kolejności zwykłej i odwróconej.

numbers = (10, 20, 30, 40, 50)  # Tworzy krotkę z pięcioma liczbami.
reversed_numbers = numbers[::-1]  # Kopiuje elementy od końca dzięki krokowi -1.
print('Tuple:', ','.join(map(str, numbers)))  # Zamienia liczby na napisy i łączy je przecinkami.
print('Reverse order:', ','.join(map(str, reversed_numbers)))  # Wypisuje liczby po odwróceniu kolejności.
