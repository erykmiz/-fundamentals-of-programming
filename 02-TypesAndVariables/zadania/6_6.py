# Zadanie 6.6: pokazujemy numery podanych znaków w standardzie Unicode.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

print(f"a {ord('a')}")  # Pokazuje znak a oraz jego numer w Unicode, czyli 97.
print(f"b {ord('b')}")  # Pokazuje znak b oraz jego numer 98.
print(f"z {ord('z')}")  # Pokazuje znak z oraz jego numer 122.
print(f"A {ord('A')}")  # Pokazuje wielkie A i jego numer 65; wielkość litery ma znaczenie.
print(f"B {ord('B')}")  # Pokazuje wielkie B i jego numer 66.
print(f"Z {ord('Z')}")  # Pokazuje wielkie Z i jego numer 90.
print(f"1 {ord('1')}")  # Pokazuje znak cyfry 1 i jego numer 49, a nie wartość liczby 1.
print(f"= {ord('=')}")  # Pokazuje znak równości i jego numer 61; tutaj = jest znakiem tekstu.
print(f"+ {ord('+')}")  # Pokazuje znak plus i jego numer 43; tutaj + nie wykonuje dodawania.
print(f"€ {ord('€')}")  # Pokazuje znak euro i jego numer 8364.
