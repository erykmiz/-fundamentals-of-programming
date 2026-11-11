# Zadanie 3.7: dzielimy ludność świata między dwie półkule na podstawie danych z ćwiczenia dla 2022 roku.

total = 8000000000  # Zapisuje całkowitą liczbę ludzi z zadania: 8 miliardów.
north = 7200000000  # Zapisuje liczbę ludzi na półkuli północnej: 7 miliardów i 200 milionów.
south = total - north  # Odejmuje mieszkańców północy od całości: 8000000000 - 7200000000 = 800000000.
print("Ludność świata:", total)  # Pokazuje całkowitą liczbę mieszkańców: 8000000000.
print("Półkula północna:", north)  # Pokazuje liczbę mieszkańców północy: 7200000000.
print("Półkula północna w %:", north / total * 100)  # Dzieli część przez całość: 0.9, a potem mnoży przez 100 i pokazuje 90.0%.
print("Półkula południowa:", south)  # Pokazuje obliczoną liczbę mieszkańców południa: 800000000.
print("Półkula południowa w %:", south / total * 100)  # Liczy 800000000 / 8000000000 * 100 i pokazuje 10.0%.
