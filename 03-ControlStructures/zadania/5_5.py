# Zadanie 5.5: suma i średnia liczb podawanych do momentu wpisania zera.
# Zero kończy wprowadzanie i nie jest uwzględniane ani w sumie, ani w liczbie danych.
total_sum = 0  # Przygotowuje sumę wszystkich zaakceptowanych liczb.
count = 0  # Przygotowuje licznik liczb potrzebny do obliczenia średniej.
while True:  # Powtarza wprowadzanie danych aż do wykonania instrukcji break.
    number = int(input("Enter a number (0 to stop): "))  # Wczytuje kolejną liczbę całkowitą.
    if number == 0:  # Sprawdza, czy użytkownik wybrał zakończenie wprowadzania danych.
        break  # Natychmiast opuszcza pętlę, nie dodając zera do danych.
    total_sum += number  # Dodaje wprowadzoną liczbę do sumy.
    count += 1  # Zwiększa liczbę zaakceptowanych wartości o jeden.
print(f"The total sum of the numbers is: {total_sum}")  # Wyświetla sumę; przy braku danych będzie to zero.
if count > 0:  # Sprawdza, czy istnieją dane, aby uniknąć dzielenia przez zero.
    average = total_sum / count  # Dzieli sumę przez liczbę danych, otrzymując średnią arytmetyczną.
    print(f"The arithmetic mean of the numbers is: {average}")  # Wyświetla obliczoną średnią.
else:  # Obsługuje sytuację, w której pierwszą wpisaną liczbą było zero.
    print("No numbers entered; arithmetic mean cannot be calculated.")  # Wyjaśnia, dlaczego nie da się obliczyć średniej.
