# Zadanie 4.1: wpisujemy dane przykładowego Adama do gotowych zdań.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

name = "Adam"  # Pod nazwą name, czyli imię, zapamiętuje tekst Adam.
age = 20  # Pod nazwą age, czyli wiek, zapamiętuje liczbę 20.
height = 180  # Pod nazwą height, czyli wzrost, zapamiętuje liczbę 180 centymetrów.

print(f"My name is {name}.")  # W miejsce {name} wstawia Adam i pokazuje zdanie.
print(f"I am {age} years old, and my height is {height} cm.")  # Wstawia 20 za {age} oraz 180 za {height}.
print(f"In 6 years I will be {age + 6} years old.")  # Liczy 20 + 6 = 26 wewnątrz {} i pokazuje przyszły wiek.
