# Zadanie 6.8: liczymy litery leżące pomiędzy dwiema podanymi literami alfabetu A-Z.
# Podaj po jednej literze A-Z; abs daje odległość, a max(0, ...) zapobiega wynikowi -1.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

first = input("Enter first letter: ").upper()  # Pobiera pierwszą literę, np. a zmienia na A i zapisuje w first.
last = input("Enter last letter: ").upper()  # Pobiera drugą literę, np. d zmienia na D i zapisuje w last.
first_letter_code = ord(first)  # ord() odczytuje numer pierwszego znaku, np. dla A jest to 65.
last_letter_code = ord(last)  # Odczytuje numer drugiego znaku, np. dla D jest to 68.

distance = abs(last_letter_code - first_letter_code)  # Liczy odległość numerów liter; abs zmienia np. -3 na 3.

number_of_letters = max(0, distance - 1)  # Odejmuje 1, aby liczyć litery pomiędzy; max daje 0 dla K/K.
print(f"Between {first} and {last} is {number_of_letters} letters")  # print() pokazuje wynik; f wstawia wartości w miejsca {}.
