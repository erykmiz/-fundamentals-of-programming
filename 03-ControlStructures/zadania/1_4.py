# Zadanie 1.4: sprawdzenie, czy saldo wystarcza na zakupy.

account_balance = 500  # Zapisuje dostępne środki: 500.
total_payment = float(input('Enter total payment: '))  # Pobiera kwotę; float pozwala wpisać np. 140.50 z kropką.
if total_payment <= account_balance:  # <= dopuszcza też równość, więc zakup za 500 można opłacić.
    print('Payment completed')  # Potwierdza płatność, gdy środków wystarcza.
else:  # Wybiera tę część, gdy kwota zakupów przekracza saldo.
    print('No funds')  # Pokazuje informację o braku środków.
