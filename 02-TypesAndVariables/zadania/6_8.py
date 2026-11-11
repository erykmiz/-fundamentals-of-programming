# Zadanie 6.8: liczba liter pomiędzy dwiema literami alfabetu A-Z.
# Podaj po jednej literze; przykłady: A i D dają 2, B i M dają 10, K i K dają 0.
first = input("Enter first letter: ").upper()  # Pobiera pierwszą literę i zamienia ją na wielką, np. a na A.
last = input("Enter last letter: ").upper()  # Pobiera drugą literę i również zamienia ją na wielką.
first_letter_code = ord(first)  # Odczytuje numer Unicode pierwszej litery.
last_letter_code = ord(last)  # Odczytuje numer Unicode drugiej litery.
distance = abs(last_letter_code - first_letter_code)  # Liczy odległość liter; abs usuwa ewentualny minus.
number_of_letters = max(0, distance - 1)  # Odejmując 1, pomija litery krańcowe; max nie pozwala uzyskać liczby ujemnej.
print(f"Between {first} and {last} is {number_of_letters} letters")  # Wyświetla liczbę liter leżących pomiędzy podanymi literami.
