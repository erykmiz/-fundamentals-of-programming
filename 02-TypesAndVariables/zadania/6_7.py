# Zadanie 6.7: pokazujemy numer Unicode każdej litery przykładowego imienia John.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

name = "John"  # Zapamiętuje przykładowe imię John; można je zastąpić własnym.

for letter in name:  # Przypisuje do letter kolejno J, o, h i n; dla John wykona 4 powtórzenia.
    print(f"The letter {letter} has a code {ord(letter)}")  # Pokazuje bieżącą literę i jej numer Unicode: 74, 111, 104 lub 110.
