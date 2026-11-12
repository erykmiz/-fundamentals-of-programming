# Zadanie 5.5: obliczamy sumę i średnią podanych liczb.
# Zero kończy wprowadzanie i nie jest liczone do średniej.
# f wstawia wartości zmiennych w miejsca {}.

total_sum = 0  # Zaczyna sumę od 0.
count = 0  # Zaczyna licznik podanych liczb od 0.
while True:  # Powtarza kod aż do wykonania break.
    number = int(input("Enter a number (0 to stop): "))  # Pobiera kolejną liczbę całkowitą.
    if number == 0:  # Sprawdza, czy wpisano zero kończące program.
        break  # Opuszcza pętlę bez dodawania zera.
    total_sum += number  # Dodaje liczbę do sumy.
    count += 1  # Zwiększa liczbę przyjętych danych o 1.
print(f"The total sum of the numbers is: {total_sum}")  # Pokazuje obliczoną sumę.
if count > 0:  # Sprawdza, czy podano dane, aby nie dzielić przez 0.
    average = total_sum / count  # Dzieli sumę przez liczbę danych, otrzymując średnią.
    print(f"The arithmetic mean of the numbers is: {average}")  # Pokazuje obliczoną średnią.
else:  # Obsługuje wpisanie zera jako pierwszej liczby.
    print("No numbers entered; arithmetic mean cannot be calculated.")  # Informuje, że nie ma danych do obliczenia średniej.
