# Zadanie 8.3: zamiana stopni Celsjusza na kelwiny i stopnie Fahrenheita.

celsius = float(input('Enter temperature in degrees Celsius: '))  # Wczytuje temperaturę w stopniach Celsjusza.
kelvin = celsius + 273.15  # Dodaje 273.15, aby przeliczyć temperaturę na kelwiny.
fahrenheit = celsius * 9 / 5 + 32  # Stosuje wzór przeliczenia stopni Celsjusza na stopnie Fahrenheita.
print(f'Temperature in Kelvin: {kelvin:.2f} K')  # Wyświetla wynik w kelwinach z dwiema cyframi po kropce.
print(f'Temperature in Fahrenheit: {fahrenheit:.2f} F')  # Wyświetla wynik w stopniach Fahrenheita z dwiema cyframi po kropce.
