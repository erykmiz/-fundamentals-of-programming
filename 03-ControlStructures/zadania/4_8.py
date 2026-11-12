# Zadanie 4.8: obliczamy ułamki od 1/1 do 1/10.
# Uwzględniamy 1/1, bo występuje w przykładowym wyniku polecenia.

for i in range(1, 11):  # Bierze mianowniki od 1 do 10; 11 nie wchodzi do zakresu.
    print(f"1/{i} = {1 / i}")  # Oblicza 1 / i; f wstawia mianownik i wynik w miejsca {}.
