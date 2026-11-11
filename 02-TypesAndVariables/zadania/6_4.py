# Zadanie 6.4: wycinamy z jednego opisu imię, nazwisko, datę urodzenia i inicjały.
# Indeksy liczymy od 0; [4:8] wybiera pozycje 4, 5, 6, 7, bez 8.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

employee = "Mr. John May, born on 1998-02-16"  # Zapamiętuje cały opis pracownika podany w zadaniu.

print(f"Name: {employee[4:8]}")  # Wybiera cztery znaki od indeksu 4 do 7 i pokazuje imię John.
print(f"Surname: {employee[9:12]}")  # Wybiera trzy znaki od indeksu 9 do 11 i pokazuje nazwisko May.
print(f"Born: {employee[22:32]}")  # Wybiera dziesięć znaków od indeksu 22 do 31 i pokazuje datę 1998-02-16.
print(f"Initials: {employee[4]}{employee[9]}")  # Pobiera samo J oraz samo M i pokazuje je obok siebie jako JM.
