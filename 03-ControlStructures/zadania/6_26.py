# Zadanie 6.26: maksymalnie trzy próby wpisania PIN-u 0805.
correct_pin = '0805'  # Zapisuje PIN jako tekst, dzięki czemu początkowe zero nie znika.
pin_ok = False  # Na początku nie otrzymaliśmy jeszcze poprawnego PIN-u.
for attempt in range(3):  # Pozwala wykonać najwyżej trzy próby.
    entered_pin = input('Enter the PIN code: ')  # Wczytuje wpisany PIN jako tekst.
    if entered_pin == correct_pin:  # Porównuje wszystkie znaki, również początkowe zero.
        pin_ok = True  # Zapamiętuje udaną weryfikację.
        print('PIN is correct')  # Informuje o poprawnym PIN-ie.
        break  # Kończy pętlę od razu po udanej próbie.
    else:  # Obsługuje niepoprawny PIN.
        print('Incorrect...')  # Informuje, że wpisany kod był błędny.
if not pin_ok:  # Sprawdza, czy żadna z trzech prób nie była poprawna.
    print('Sorry, your payment card has been blocked.')  # Wyświetla blokadę dopiero po trzech nieudanych próbach.
