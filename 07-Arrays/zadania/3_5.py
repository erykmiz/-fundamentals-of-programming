# Zadanie 3.5. Podnosimy każdy element tablicy do kwadratu.

numbers = [8, 2, 5, 1, 9]  # Zapisuje przykładowe liczby.
squares = []  # Tworzy pustą listę na kwadraty liczb.
for number in numbers:  # Pobiera po kolei każdą liczbę.
    squares.append(number ** 2)  # Oblicza drugą potęgę i dopisuje ją do wyników.
print('Array:', *numbers)  # Wyświetla pierwotne liczby oddzielone spacjami.
print('2nd power:', *squares)  # Wyświetla kwadraty w tej samej kolejności.
