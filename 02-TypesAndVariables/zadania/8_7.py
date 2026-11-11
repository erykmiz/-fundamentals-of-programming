# Zadanie 8.7: zapis liczby całkowitej w systemie dwójkowym i szesnastkowym.
# Przykład: 125 -> 0b1111101 w systemie dwójkowym oraz 0x7d w szesnastkowym.

number = int(input('Enter number: '))  # Wczytuje liczbę całkowitą zapisaną dziesiętnie.
print(f'Binary number: {bin(number)}')  # Funkcja bin() zwraca zapis dwójkowy z przedrostkiem 0b.
print(f'Hexadecimal number: {hex(number)}')  # Funkcja hex() zwraca zapis szesnastkowy z przedrostkiem 0x.
