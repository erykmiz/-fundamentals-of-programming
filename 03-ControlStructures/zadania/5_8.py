# Zadanie 5.8: edukacyjny symulator bankomatu z opcją sprawdzenia i zmiany PIN-u.
# To samodzielne rozwiązanie programu atm.py; PIN pozostaje tekstem, aby zachować początkowe zera.
balance = 1000  # Ustawia początkowe saldo przykładowego konta.
pin = "1111"  # Zapisuje początkowy czterocyfrowy PIN podany w programie źródłowym.
while True:  # Pokazuje menu ponownie po każdej operacji aż do wybrania wyjścia.
    print()  # Wstawia pustą linię, aby kolejne menu było czytelne.
    print("ATM Menu:")  # Wyświetla tytuł menu.
    print("1. Check balance")  # Pokazuje numer opcji sprawdzającej saldo.
    print("2. Deposit")  # Pokazuje numer opcji wpłacającej pieniądze.
    print("3. Withdraw")  # Pokazuje numer opcji wypłacającej pieniądze.
    print("4. Exit")  # Pokazuje numer opcji kończącej program.
    print("5. Check PIN")  # Pokazuje nową opcję sprawdzania poprawności PIN-u.
    print("6. Change PIN")  # Pokazuje nową opcję zmiany PIN-u.
    choice = input("Choose an option (1-6): ")  # Wczytuje numer wybranej opcji jako tekst.
    if choice == "1":  # Sprawdza, czy wybrano wyświetlenie salda.
        print(f"Your current balance is: €{balance:.2f}")  # Wyświetla saldo z dwiema cyframi po kropce.
    elif choice == "2":  # Sprawdza, czy wybrano wpłatę.
        amount = float(input("Enter the amount to deposit: "))  # Wczytuje kwotę wpłaty jako liczbę.
        if amount > 0:  # Zezwala na wpłatę tylko dodatniej kwoty.
            balance += amount  # Dodaje wpłatę do obecnego salda.
            print(f"€{amount:.2f} has been deposited. New balance: €{balance:.2f}")  # Potwierdza wpłatę i wyświetla nowe saldo.
        else:  # Obsługuje kwotę równą zero lub ujemną.
            print("Amount must be positive.")  # Wyjaśnia, dlaczego kwota nie została wpłacona.
    elif choice == "3":  # Sprawdza, czy wybrano wypłatę.
        amount = float(input("Enter the amount to withdraw: "))  # Wczytuje kwotę wypłaty jako liczbę.
        if amount <= 0:  # Odrzuca zerową lub ujemną wypłatę.
            print("Amount must be positive.")  # Informuje, że kwota musi być dodatnia.
        elif amount <= balance:  # Sprawdza, czy na koncie jest wystarczająco dużo pieniędzy.
            balance -= amount  # Odejmuje wypłatę od salda.
            print(f"€{amount:.2f} has been withdrawn. New balance: €{balance:.2f}")  # Potwierdza wypłatę i pokazuje pozostałe saldo.
        else:  # Obsługuje próbę wypłacenia kwoty większej od salda.
            print("Insufficient balance.")  # Informuje o niewystarczających środkach.
    elif choice == "4":  # Sprawdza, czy użytkownik chce zakończyć działanie symulatora.
        print("Exiting... Thank you for using the ATM!")  # Wyświetla wiadomość pożegnalną.
        break  # Opuszcza pętlę i kończy program.
    elif choice == "5":  # Obsługuje nową opcję sprawdzenia PIN-u.
        entered_pin = input("Enter your PIN: ")  # Pobiera PIN jako tekst, aby nie usunąć zer na początku.
        if entered_pin == pin:  # Porównuje wpisany PIN z obecnie zapisanym PIN-em.
            print("PIN is correct.")  # Potwierdza zgodność obu PIN-ów.
        else:  # Obsługuje wpisanie innego PIN-u.
            print("Incorrect PIN.")  # Informuje o błędnym PIN-ie.
    elif choice == "6":  # Obsługuje nową opcję zmiany PIN-u.
        entered_pin = input("Enter your current PIN: ")  # Prosi o obecny PIN przed umożliwieniem zmiany.
        if entered_pin == pin:  # Pozwala przejść dalej tylko przy poprawnym obecnym PIN-ie.
            new_pin = input("Enter a new 4-digit PIN: ")  # Pobiera nowy PIN w postaci tekstu.
            if len(new_pin) == 4 and new_pin.isdigit():  # Wymaga dokładnie czterech znaków i sprawdza, czy wszystkie są cyframi.
                pin = new_pin  # Zastępuje stary PIN nowym, zachowując również początkowe zera.
                print("PIN changed successfully.")  # Potwierdza zapisanie nowego PIN-u.
            else:  # Obsługuje nieprawidłową długość lub obecność znaków innych niż cyfry.
                print("PIN must contain exactly 4 digits.")  # Wyjaśnia wymagany format nowego PIN-u.
        else:  # Obsługuje podanie niepoprawnego obecnego PIN-u.
            print("Incorrect PIN. PIN was not changed.")  # Informuje, że obecny PIN pozostał bez zmiany.
    else:  # Obsługuje numer opcji, którego nie ma w menu.
        print("Invalid option. Please try again.")  # Prosi o wybranie jednej z sześciu dostępnych opcji.
