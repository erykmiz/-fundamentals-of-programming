# Zadanie 6.16: czas prania z opcjonalnym płukaniem i wirowaniem.
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ').strip().lower()  # Wczytuje wybór programu i zamienia litery na małe.
extra_rinse = input('Extra rinse? (y/n): ').strip().lower() == 'y'  # Zapisuje True, jeśli wybrano dodatkowe płukanie.
extra_spin = input('Extra spin? (y/n): ').strip().lower() == 'y'  # Zapisuje True, jeśli wybrano dodatkowe wirowanie.
total_washing_time = 0  # Przygotowuje zmienną na łączny czas w minutach.
if program == 'j':  # Rozpoznaje wybór prania kurtki.
    total_washing_time = 40  # Przypisuje kurtce 40 minut prania.
elif program == 'u':  # Rozpoznaje wybór prania bielizny.
    total_washing_time = 70  # Przypisuje bieliźnie 70 minut prania.
elif program == 's':  # Rozpoznaje wybór prania butów.
    total_washing_time = 20  # Przypisuje butom 20 minut prania.
if program == 'j' or program == 'u' or program == 's':  # Oblicza dodatki tylko po wybraniu istniejącego programu.
    if extra_rinse:  # Sprawdza, czy ma być wykonane dodatkowe płukanie.
        total_washing_time += 15  # Dodaje 15 minut do dotychczasowego czasu.
    if extra_spin:  # Sprawdza, czy ma być wykonane dodatkowe wirowanie.
        total_washing_time += 9  # Dodaje 9 minut do dotychczasowego czasu.
    print(f'Total washing time: {total_washing_time} minutes')  # Wyświetla sumę czasu programu i wybranych dodatków.
else:  # Obsługuje znak inny niż j, u lub s.
    print('Incorrect washing program')  # Informuje, że nie rozpoznano wybranego programu.
