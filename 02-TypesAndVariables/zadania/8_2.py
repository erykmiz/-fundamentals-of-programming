# Zadanie 8.2: obliczamy pole koła i długość jego obwodu na podstawie promienia.
# Używamy pi = 3.14, zgodnie z przykładowymi wynikami w zadaniu.
# f wstawia wartości z {}; :.2f pokazuje 2 miejsca po kropce, bez zmiany wartości zmiennej.

radius = float(input('Enter circle radius: '))  # Pyta o promień koła i zapisuje go jako liczbę pod nazwą radius.
pi = 3.14  # Zapisuje przybliżenie pi; znak = oznacza zapamiętanie wartości pod wybraną nazwą.
area = pi * radius ** 2  # Oblicza pole ze wzoru pi * promień * promień; dla promienia 3 jest to około 28.26.
circumference = 2 * pi * radius  # Oblicza obwód ze wzoru 2 * pi * promień; dla promienia 3 otrzymuje 18.84.
print(f'Area: {area:.2f}')  # Wyświetla pole, np. 28.26 dla promienia 3 albo 3.14 dla promienia 1.
print(f'Circumference: {circumference:.2f}')  # Wyświetla obwód, np. 18.84 dla promienia 3 albo 6.28 dla promienia 1.
