# Zadanie 5.4: obliczenie 23% podanej kwoty, zgodnie z przykładem w zadaniu.
# Kwotę dziesiętną wpisuj z kropką, np. 15.84.
amount = float(input("Enter amount: "))  # Pobiera kwotę i zamienia tekst na liczbę.
vat = amount * 0.23  # Oblicza 23% kwoty, czyli 23 setne jej wartości.
print(f"Amount  : {amount:6.2f}")  # Wyświetla kwotę w polu szerokości 6 znaków, z dwoma miejscami po przecinku.
print(f"VAT 23% : {vat:6.2f}")  # Wyświetla podatek w tym samym formacie; dla 15.84 otrzymasz 3.64.
