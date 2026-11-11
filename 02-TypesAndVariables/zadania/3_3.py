# Zadanie 3.3: zamiana wartości x i y za pomocą zmiennej pomocniczej z.

x = 7  # Nadaje zmiennej x początkową wartość 7.
y = 34  # Nadaje zmiennej y początkową wartość 34.
z = 0  # Przygotowuje pomocniczą zmienną, która na chwilę przechowa wartość x.
print("Przed zamianą: x =", x, "y =", y)  # Wyświetla wartości przed ich zamianą.
z = x  # Zapamiętuje dotychczasową wartość x, czyli 7, aby jej nie stracić.
x = y  # Kopiuje wartość 34 ze zmiennej y do zmiennej x.
y = z  # Kopiuje zapamiętaną wartość 7 ze zmiennej z do zmiennej y.
print("Po zamianie: x =", x, "y =", y)  # Wyświetla wynik: x ma wartość 34, a y ma wartość 7.
