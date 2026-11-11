# Zadanie 6.15: sprawdzenie 13 cyfr i prefiksu numeru artykułu.
# Zgodnie z ćwiczeniem sprawdzamy format, bez obliczania cyfry kontrolnej EAN-13.
# Prefiks 590 sprawdzamy według polecenia; sam prefiks nie gwarantuje kraju produkcji.
article_number = input('Enter EAN-13 article number: ')  # Pobiera numer jako tekst, zachowując ewentualne zera na początku.
if len(article_number) == 13 and article_number.isascii() and article_number.isdigit():  # Wymaga dokładnie 13 zwykłych cyfr od 0 do 9.
    print('Article number is correct')  # Potwierdza poprawność formatu wymaganego w zadaniu.
    if article_number[0:3] == '590':  # Sprawdza prefiks dopiero po potwierdzeniu prawidłowego formatu.
        print('Article manufactured in Poland')  # Wyświetla komunikat przypisany prefiksowi 590 w ćwiczeniu.
else:  # Wykonuje tę część dla numeru o błędnej długości lub zawierającego inne znaki.
    print('Incorrect article number')  # Informuje, że numer nie spełnia wymaganego formatu.
