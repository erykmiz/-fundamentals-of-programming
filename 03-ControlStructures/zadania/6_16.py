# Zadanie 6.16: Liczymy czas prania z płukaniem i wirowaniem.
# strip() usuwa skrajne spacje, lower() zmienia litery na małe; == porównuje, = zapisuje.
# Dwa osobne if pozwalają dodać zarówno płukanie, jak i wirowanie; += dodaje do obecnego czasu.

program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ').strip().lower()  # Pobiera symbol programu: j, u albo s.
extra_rinse = input('Extra rinse? (y/n): ').strip().lower() == 'y'  # Zapisuje True, jeśli odpowiedź o płukaniu to y.
extra_spin = input('Extra spin? (y/n): ').strip().lower() == 'y'  # Zapisuje True, jeśli odpowiedź o wirowaniu to y.
total_washing_time = 0  # Zaczyna liczenie czasu od zera.
if program == 'j':  # Sprawdza, czy wybrano kurtkę.
    total_washing_time = 40  # Ustawia 40 minut prania kurtki.
elif program == 'u':  # Sprawdza, czy wybrano bieliznę.
    total_washing_time = 70  # Ustawia 70 minut prania bielizny.
elif program == 's':  # Sprawdza, czy wybrano buty.
    total_washing_time = 20  # Ustawia 20 minut prania butów.
if program == 'j' or program == 'u' or program == 's':  # Dolicza dodatki tylko dla poprawnego programu.
    if extra_rinse:  # Sprawdza, czy wybrano płukanie.
        total_washing_time += 15  # Dodaje 15 minut płukania.
    if extra_spin:  # Sprawdza, czy wybrano wirowanie.
        total_washing_time += 9  # Dodaje 9 minut wirowania.
    print(f'Total washing time: {total_washing_time} minutes')  # Pokazuje łączny czas w minutach.
else:  # Obsługuje symbol inny niż j, u lub s.
    print('Incorrect washing program')  # Informuje o błędnym programie.
