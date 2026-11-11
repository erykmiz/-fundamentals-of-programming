# Zadanie 8.5: odczytanie kodu banku i kraju z kodu SWIFT.
# Przykłady: BPKOPLPW -> BPKO i PL; CHASUS33 -> CHAS i US; DEUTDEFF -> DEUT i DE.

swift = input('Enter SWIFT code: ').strip().upper()  # Wczytuje kod SWIFT, usuwa skrajne spacje i zamienia litery na wielkie.
bank_code = swift[0:4]  # Pobiera cztery pierwsze znaki; znak o indeksie 4 nie należy do tego fragmentu.
country_code = swift[4:6]  # Pobiera znaki o indeksach 4 i 5, czyli dwuliterowy kod kraju.
print(f'Bank Code: {bank_code}')  # Wyświetla odczytany kod banku.
print(f'Country Code: {country_code}')  # Wyświetla odczytany kod kraju.
