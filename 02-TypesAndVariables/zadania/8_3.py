# Zadanie 8.3: przeliczamy temperaturę ze stopni Celsjusza na kelwiny i stopnie Fahrenheita.
# f wstawia wartości z {}; :.2f pokazuje 2 miejsca po kropce, bez zmiany wartości zmiennej.

celsius = float(input('Enter temperature in degrees Celsius: '))  # Pyta o stopnie Celsjusza i zapamiętuje podaną liczbę jako celsius.
kelvin = celsius + 273.15  # Dodaje 273.15 zgodnie ze wzorem na kelwiny; dla 0 stopni Celsjusza otrzymuje 273.15 K.
fahrenheit = celsius * 9 / 5 + 32  # Przelicza temperaturę na Fahrenheita; dla 0 stopni Celsjusza wynikiem jest 32.
print(f'Temperature in Kelvin: {kelvin:.2f} K')  # Wyświetla temperaturę w kelwinach, np. 273.15 K dla wejścia 0.
print(f'Temperature in Fahrenheit: {fahrenheit:.2f} F')  # Wyświetla temperaturę Fahrenheita, np. 32.00 F dla wejścia 0.
