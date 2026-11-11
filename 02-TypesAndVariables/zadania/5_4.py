# Zadanie 5.4: liczymy 23% podanej kwoty, zgodnie z przykładem w poleceniu.
# f wstawia wartości z {}; :6.2f daje 2 miejsca po kropce w polu szerokości co najmniej 6 znaków.

amount = float(input("Enter amount: "))  # Pyta o kwotę, np. 15.84 z kropką, i zapisuje liczbę w amount.
vat = amount * 0.23  # Mnoży podaną kwotę przez 23/100, czyli liczy 23% tej kwoty.

print(f"Amount  : {amount:6.2f}")  # Pokazuje podaną kwotę z dwiema cyframi po kropce.
print(f"VAT 23% : {vat:6.2f}")  # Pokazuje obliczone 23%; np. wynik 3.6432 wyświetli jako 3.64.
