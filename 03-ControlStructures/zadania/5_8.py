# Zadanie 5.8: bankomat ze sprawdzaniem i zmianą PIN-u.
# PIN jest tekstem, aby zachować początkowe zera; len() liczy znaki, isdigit() sprawdza cyfry.
# f wstawia wartości z {}; :.2f pokazuje 2 miejsca po kropce.

balance = 1000  # Ustawia początkowe saldo na 1000.
pin = "1111"  # Zapisuje PIN jako tekst, a nie liczbę.
while True:  # Powtarza menu aż do wybrania wyjścia.
    print()  # Wstawia pustą linię między kolejnymi menu.
    print("ATM Menu:")  # Pokazuje tytuł menu.
    print("1. Check balance")  # Pokazuje opcję sprawdzenia salda.
    print("2. Deposit")  # Pokazuje opcję wpłaty.
    print("3. Withdraw")  # Pokazuje opcję wypłaty.
    print("4. Exit")  # Pokazuje opcję wyjścia.
    print("5. Check PIN")  # Pokazuje opcję sprawdzenia PIN-u.
    print("6. Change PIN")  # Pokazuje opcję zmiany PIN-u.
    choice = input("Choose an option (1-6): ")  # Pobiera numer opcji jako tekst.
    if choice == "1":  # Sprawdza, czy wybrano saldo.
        print(f"Your current balance is: €{balance:.2f}")  # Pokazuje saldo z dwoma miejscami po kropce.
    elif choice == "2":  # Sprawdza, czy wybrano wpłatę.
        amount = float(input("Enter the amount to deposit: "))  # Pobiera kwotę i zamienia tekst na liczbę.
        if amount > 0:  # Wymaga kwoty większej od zera.
            balance += amount  # Dodaje wpłatę do salda.
            print(f"€{amount:.2f} has been deposited. New balance: €{balance:.2f}")  # Potwierdza wpłatę i pokazuje nowe saldo.
        else:  # Obsługuje kwotę zerową lub ujemną.
            print("Amount must be positive.")  # Informuje, że kwota musi być dodatnia.
    elif choice == "3":  # Sprawdza, czy wybrano wypłatę.
        amount = float(input("Enter the amount to withdraw: "))  # Pobiera kwotę wypłaty jako liczbę.
        if amount <= 0:  # Sprawdza, czy kwota jest zerowa lub ujemna.
            print("Amount must be positive.")  # Odrzuca kwotę niedodatnią.
        elif amount <= balance:  # Sprawdza, czy saldo wystarcza na wypłatę.
            balance -= amount  # Odejmuje wypłatę od salda.
            print(f"€{amount:.2f} has been withdrawn. New balance: €{balance:.2f}")  # Potwierdza wypłatę i pokazuje nowe saldo.
        else:  # Obsługuje wypłatę większą od salda.
            print("Insufficient balance.")  # Informuje o braku środków.
    elif choice == "4":  # Sprawdza, czy wybrano wyjście.
        print("Exiting... Thank you for using the ATM!")  # Pokazuje pożegnanie.
        break  # Kończy pętlę i działanie symulatora.
    elif choice == "5":  # Sprawdza, czy wybrano weryfikację PIN-u.
        entered_pin = input("Enter your PIN: ")  # Pobiera PIN jako tekst, zachowując początkowe zera.
        if entered_pin == pin:  # Porównuje wpisany PIN z zapisanym; == sprawdza równość.
            print("PIN is correct.")  # Potwierdza poprawny PIN.
        else:  # Obsługuje niepoprawny PIN.
            print("Incorrect PIN.")  # Pokazuje informację o błędzie.
    elif choice == "6":  # Sprawdza, czy wybrano zmianę PIN-u.
        entered_pin = input("Enter your current PIN: ")  # Pobiera obecny PIN przed zmianą.
        if entered_pin == pin:  # Pozwala zmienić PIN tylko po podaniu poprawnego obecnego PIN-u.
            new_pin = input("Enter a new 4-digit PIN: ")  # Pobiera nowy PIN jako tekst.
            if len(new_pin) == 4 and new_pin.isdigit():  # Wymaga 4 znaków i samych cyfr; and wymaga obu warunków.
                pin = new_pin  # Zapisuje nowy PIN zamiast starego.
                print("PIN changed successfully.")  # Potwierdza zmianę PIN-u.
            else:  # Obsługuje błędny format nowego PIN-u.
                print("PIN must contain exactly 4 digits.")  # Przypomina wymóg czterech cyfr.
        else:  # Obsługuje błędny obecny PIN.
            print("Incorrect PIN. PIN was not changed.")  # Informuje, że PIN nie został zmieniony.
    else:  # Obsługuje opcję spoza menu.
        print("Invalid option. Please try again.")  # Prosi o poprawny numer opcji.
