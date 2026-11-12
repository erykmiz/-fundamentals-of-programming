# Zadanie 6.26: Sprawdzamy PIN 0805 w najwyżej trzech próbach.
# PIN jest tekstem, aby zachować początkowe zero; break kończy pętlę od razu po trafieniu.

correct_pin = '0805'  # Zapisuje poprawny PIN jako tekst 0805.
pin_ok = False  # Zapisuje, że na razie nie wpisano poprawnego PIN-u.
for attempt in range(3):  # Pozwala wykonać najwyżej 3 próby.
    entered_pin = input('Enter the PIN code: ')  # Pobiera wpisany PIN jako tekst.
    if entered_pin == correct_pin:  # Sprawdza, czy wpisany PIN jest równy poprawnemu.
        pin_ok = True  # Zapamiętuje, że PIN był poprawny.
        print('PIN is correct')  # Potwierdza poprawny PIN.
        break  # Kończy próby po poprawnej odpowiedzi.
    else:  # Obsługuje błędny PIN.
        print('Incorrect...')  # Pokazuje informację o błędnym PIN-ie.
if not pin_ok:  # not pin_ok jest prawdą, gdy nie trafiono PIN-u.
    print('Sorry, your payment card has been blocked.')  # Pokazuje blokadę po trzech nieudanych próbach.
