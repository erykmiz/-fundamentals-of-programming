# Zadanie 5.3: pytamy o imię, dopóki nie zostanie wpisane.
# input() daje tekst; strip() usuwa spacje z początku i końca.

name = ""  # Zaczyna od pustego tekstu, aby uruchomić pętlę.
while name == "":  # Powtarza pytanie, dopóki imię jest puste; == porównuje.
    name = input("Enter your name: ").strip()  # Pobiera imię i usuwa skrajne spacje.
print(f"Hello {name}")  # Wstawia imię w {name} i pokazuje powitanie.
