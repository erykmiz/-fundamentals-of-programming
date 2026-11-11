# Zadanie 1.3: kalkulator BMI uruchamiany jako plik .py.
# W terminalu otwartym w folderze zadania uruchom: py 1_3.py.
# Przykładowe dane do sprawdzenia obliczeń: wzrost 180 cm, masa 75 kg; wynik: 23.15.

height = input("Podaj wzrost w cm: ")  # Pobiera wzrost z klawiatury; input() zwraca tekst.
weight = input("Podaj masę w kg: ")  # Pobiera masę z klawiatury jako tekst.
height = int(height)  # Zamienia tekst ze wzrostem na liczbę całkowitą, np. "180" na 180.
weight = int(weight)  # Zamienia tekst z masą na liczbę całkowitą, np. "75" na 75.
bmi = weight / (height / 100) ** 2  # Zamienia centymetry na metry i dzieli masę przez kwadrat wzrostu.
bmi = round(bmi, 2)  # Zaokrągla obliczoną wartość do dwóch miejsc po przecinku.
print("Twoje BMI:", bmi)  # Wyświetla wynik obliczeń.
