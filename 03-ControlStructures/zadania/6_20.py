# Zadanie 6.20: Tworzymy zapis dwójkowy przez dzielenie przez 2.
# % 2 daje kolejną cyfrę 0 lub 1, a // 2 daje całkowity iloraz; cyfry dopisujemy z lewej.

decimal_number = int(input('Enter decimal number: '))  # Pobiera liczbę całkowitą w zapisie dziesiętnym.
remaining = abs(decimal_number)  # abs usuwa ewentualny minus na czas obliczeń.
binary_number = ''  # Przygotowuje pusty tekst na wynik.
while remaining > 0:  # Powtarza dzielenie, dopóki została liczba większa od zera.
    remainder = remaining % 2  # Oblicza resztę z dzielenia przez 2.
    binary_number = str(remainder) + binary_number  # str zamienia resztę na tekst i dopisuje ją z lewej strony.
    remaining = remaining // 2  # Dzieli pozostałą liczbę przez 2 bez części ułamkowej.
if binary_number == '':  # Sprawdza, czy pętla nie zapisała żadnej cyfry.
    binary_number = '0'  # Ustawia wynik 0 dla wejścia równego zero.
if decimal_number < 0:  # Sprawdza, czy liczba wejściowa była ujemna.
    binary_number = '-' + binary_number  # Przywraca minus przed wynikiem.
print(f'{decimal_number}(10) = {binary_number}(2)')  # Pokazuje oba zapisy, np. 12(10) = 1100(2).
