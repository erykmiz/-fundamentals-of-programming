# Zadanie 8.7: tę samą liczbę całkowitą pokazujemy w systemie dwójkowym i szesnastkowym.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

number = int(input('Enter number: '))  # Pyta o liczbę zapisaną dziesiętnie i zapamiętuje ją pod nazwą number.
print(f'Binary number: {bin(number)}')  # bin tworzy zapis dwójkowy z 0b, np. 125 daje 0b1111101.
print(f'Hexadecimal number: {hex(number)}')  # hex tworzy zapis szesnastkowy z 0x, np. 125 daje 0x7d.
