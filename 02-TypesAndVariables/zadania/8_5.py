# Zadanie 8.5: odczytujemy kod banku i kod kraju z tekstowego kodu SWIFT.
# strip() usuwa skrajne spacje, upper() zmienia litery na wielkie.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

swift = input('Enter SWIFT code: ').strip().upper()  # Pyta o kod, porządkuje jego zapis i zapamiętuje tekst pod nazwą swift.
bank_code = swift[0:4]  # Wybiera znaki z pozycji 0, 1, 2 i 3; dla BPKOPLPW otrzymuje BPKO.
country_code = swift[4:6]  # Wybiera znaki z pozycji 4 i 5; dla BPKOPLPW otrzymuje PL.
print(f'Bank Code: {bank_code}')  # Wyświetla wybrane cztery znaki kodu banku.
print(f'Country Code: {country_code}')  # Wyświetla wybrane dwa znaki kodu kraju.
