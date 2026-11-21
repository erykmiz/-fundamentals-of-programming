# Zadanie 1.11. Obliczamy statystyki dla 30 pomiarów temperatury podanych w poleceniu.

temperatures = [  # Zapisuje pomiary w kolejności ich wykonania.
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3,  # Zapisuje pierwszych dziesięć pomiarów.
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,  # Zapisuje kolejnych dziesięć pomiarów.
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7,  # Zapisuje ostatnich dziesięć pomiarów.
]  # Kończy listę pomiarów.

measurements = len(temperatures)  # Zlicza wszystkie podane pomiary.
temp_total = 0  # Ustawia początkową sumę temperatur.
for temp in temperatures:  # Odczytuje po kolei każdą temperaturę.
    temp_total += temp  # Dodaje bieżącą temperaturę do sumy.
avg_temp = temp_total / measurements  # Dzieli sumę przez liczbę pomiarów, aby obliczyć średnią.
min_temp = min(temperatures)  # Znajduje najmniejszą temperaturę na liście.
max_temp = max(temperatures)  # Znajduje największą temperaturę na liście.

negative_temp = 0  # Ustawia początkową liczbę dni z ujemną temperaturą.
index = 0  # Rozpoczyna sprawdzanie listy od pierwszego pomiaru.
while index < measurements:  # Wykonuje pętlę dla każdego poprawnego indeksu.
    if temperatures[index] < 0:  # Sprawdza, czy pomiar dla tego dnia jest poniżej zera.
        negative_temp += 1  # Dolicza dzień z ujemną temperaturą.
    index += 1  # Przechodzi do następnego pomiaru.

print('TEMPERATURE REPORT')  # Wypisuje tytuł raportu.
print('Month: March')  # Wypisuje nazwę analizowanego miesiąca.
print('Number of measurements:', measurements)  # Wyświetla liczbę pomiarów z listy.
print('Average temperature in the month:', avg_temp)  # Wyświetla obliczoną średnią.
print('Minimum temperature:', min_temp)  # Wyświetla najniższą temperaturę.
print('Maximum temperature:', max_temp)  # Wyświetla najwyższą temperaturę.
print('Number of days with negative temperature:', negative_temp)  # Wyświetla wynik zliczania ujemnych pomiarów.
