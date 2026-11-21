# Zadanie 2.1. Korzystamy z funkcji wbudowanych Pythona.

max_number = max(7, 5, 6, 3, 8, 2)  # max wybiera największą z podanych liczb.
print('Max number of 7,5,6,3,8,2 is', max_number)  # Wyświetla znalezione maksimum.

min_number = min(4, 7, 2, 3, 9, 8)  # min wybiera najmniejszą z podanych liczb.
print('Min number of 4,7,2,3,9,8 is', min_number)  # Wyświetla znalezione minimum.

phrase_length = len('computer science')  # len liczy wszystkie znaki, w tym spację.
print('The number of characters in "computer science" is', phrase_length)  # Pokazuje długość.

letter = input('Enter a letter: ')  # input wyświetla pytanie i odczytuje tekst z klawiatury.
print('Entered letter:', letter)  # Wyświetla wpisaną literę.

number = int('20303')  # int zamienia tekst z cyframi na liczbę całkowitą.
print('"20303" as an integer is', number)  # Pokazuje liczbę po zamianie.

binary = bin(304)  # bin zwraca zapis dwójkowy jako tekst zaczynający się od 0b.
print('304 in binary is', binary)  # Wyświetla zapis dwójkowy liczby 304.

hexadecimal = hex(304)  # hex zwraca zapis szesnastkowy jako tekst zaczynający się od 0x.
print('304 in hexadecimal is', hexadecimal)  # Wyświetla zapis szesnastkowy liczby 304.

euro_code = ord('€')  # ord zwraca kod Unicode pojedynczego znaku w postaci liczby.
print('The Unicode code of € is', euro_code)  # Wyświetla kod znaku euro.

absolute_value = abs(-17)  # abs oblicza odległość liczby od zera.
print('The absolute value of -17 is', absolute_value)  # Wyświetla wartość bezwzględną.
