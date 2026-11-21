# Moduł do zadania 7.6. Zostawiamy widoczne pierwsze dwie i ostatnie cztery cyfry.


def hide(card_number):  # Przyjmuje numer karty zapisany jako tekst.
    if len(card_number) != 16 or not card_number.isascii() or not card_number.isdigit():  # Wymaga 16 znaków od 0 do 9.
        raise ValueError('Card number must contain exactly 16 digits')  # Zgłasza błąd dla nieprawidłowego formatu.
    return card_number[:2] + '*' * 10 + card_number[-4:]  # Łączy początek, dziesięć gwiazdek i koniec numeru.
