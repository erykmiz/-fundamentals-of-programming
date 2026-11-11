# Zadanie 6.20: zapis dwójkowy przez kolejne dzielenie przez 2.
decimal_number = int(input('Enter decimal number: '))  # Wczytuje liczbę całkowitą w systemie dziesiętnym.
remaining = abs(decimal_number)  # Pobiera wartość bez znaku, aby dzielić także liczby ujemne.
binary_number = ''  # Przygotowuje pusty tekst na cyfry wyniku.
while remaining > 0:  # Powtarza dzielenie, dopóki iloraz nie stanie się zerem.
    remainder = remaining % 2  # Odczytuje resztę z dzielenia przez 2: zawsze 0 lub 1.
    binary_number = str(remainder) + binary_number  # Dopisuje nową cyfrę z lewej strony, czyli w odwróconej kolejności reszt.
    remaining = remaining // 2  # Zastępuje liczbę całkowitym ilorazem z dzielenia przez 2.
if binary_number == '':  # Sprawdza, czy wejściem było zero i pętla nie zapisała żadnej cyfry.
    binary_number = '0'  # Ustawia zapis dwójkowy zera na pojedyncze 0.
if decimal_number < 0:  # Sprawdza, czy trzeba odtworzyć znak liczby wejściowej.
    binary_number = '-' + binary_number  # Dopisuje minus przed dwójkowym zapisem wartości bezwzględnej.
print(f'{decimal_number}(10) = {binary_number}(2)')  # Wyświetla liczbę dziesiętną i jej zapis dwójkowy.
