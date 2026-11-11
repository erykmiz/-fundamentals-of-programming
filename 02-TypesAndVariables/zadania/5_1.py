# Zadanie 5.1: pytamy o imię i nazwisko, a następnie łączymy je w jeden tekst.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

first_name = input("Enter your first name: ")  # Prosi o imię i zapisuje wpisany tekst pod nazwą first_name.
last_name = input("Enter your last name: ")  # Prosi o nazwisko i zapisuje odpowiedź pod nazwą last_name.
full_name = first_name + " " + last_name  # Łączy imię, jedną spację i nazwisko, np. Anna May.

print(f"Your first name is {first_name} and your last name is {last_name}")  # Pokazuje podane imię i nazwisko w zdaniu.
print(f"And your full name is {full_name}")  # Pokazuje połączony tekst full_name, np. Anna May.
