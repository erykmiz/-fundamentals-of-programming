# Zadanie 1.3: program wczytuje wzrost i masę, a potem oblicza wartość BMI.

height = input("Podaj wzrost w cm: ")  # Zapisuje wpisany wzrost jako tekst, np. "180", pod nazwą height.
weight = input("Podaj masę w kg: ")  # Czeka na wpisanie masy i zapisuje tekst, np. "75", pod nazwą weight.
height = int(height)  # int zamienia tekst "180" na liczbę całkowitą 180; zapisuje liczbę z powrotem w height.
weight = int(weight)  # Zamienia tekst "75" na liczbę całkowitą 75, aby można było wykonywać obliczenia.
bmi = weight / (height / 100) ** 2  # Dzieli masę przez kwadrat wzrostu w metrach: 75 / 3.24, czyli około 23.148.
bmi = round(bmi, 2)  # round zaokrągla wynik do 2 miejsc po kropce; w bmi zostaje 23.15.
print("Twoje BMI:", bmi)  # print pokazuje podpis i obliczoną liczbę; dla przykładu 180 cm i 75 kg jest to 23.15.
