# Zadanie 3.7: podział ludności między półkulami według danych z zadania dla 2022 roku.

total = 8000000000  # Zapisuje przyjętą w zadaniu liczbę mieszkańców świata: 8 miliardów.
north = 7200000000  # Zapisuje liczbę mieszkańców półkuli północnej: 7.2 miliarda.
south = total - north  # Oblicza liczbę mieszkańców półkuli południowej: 800 milionów.
print("Ludność świata:", total)  # Wyświetla całkowitą liczbę mieszkańców.
print("Półkula północna:", north)  # Wyświetla liczbę mieszkańców półkuli północnej.
print("Półkula północna w %:", north / total * 100)  # Dzieli liczbę mieszkańców północy przez całość i mnoży przez 100; wynik: 90.0%.
print("Półkula południowa:", south)  # Wyświetla liczbę mieszkańców półkuli południowej.
print("Półkula południowa w %:", south / total * 100)  # Oblicza procent mieszkańców południa; wynik: 10.0%.
