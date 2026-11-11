# Zadanie 6.8: sprawdzenie, czy obie osoby są pełnoletnie.
person1_name = input('Enter first person name: ')  # Pobiera imię pierwszej osoby.
person1_age = int(input('Enter first person age: '))  # Pobiera wiek pierwszej osoby jako liczbę całkowitą.
person2_name = input('Enter second person name: ')  # Pobiera imię drugiej osoby.
person2_age = int(input('Enter second person age: '))  # Pobiera wiek drugiej osoby.
if person1_age >= 18 and person2_age >= 18:  # Wymaga, aby każda z obu osób miała co najmniej 18 lat.
    print(f'Both {person1_name} and {person2_name} are adults')  # Informuje, że obie osoby są pełnoletnie.
else:  # Wybiera tę część, gdy przynajmniej jedna osoba ma mniej niż 18 lat.
    print(f'Either {person1_name} or {person2_name} is not an adult')  # Informuje o niespełnieniu warunku przez przynajmniej jedną osobę.
