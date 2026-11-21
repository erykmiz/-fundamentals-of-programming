# Zadanie 4.5. Przyznajemy ocenę według progów sprawdzanych od najwyższego.

def pts_to_grade(points):  # Przyjmuje liczbę punktów zdobytych w teście.
    if points >= 18:  # Sprawdza najwyższy próg od 18 punktów.
        return 'Excellent'  # Zwraca najwyższą ocenę i kończy działanie funkcji.
    if points >= 14:  # Sprawdza, czy wynik jest w przedziale od 14 do 17 punktów.
        return 'Good'  # Zwraca ocenę dobrą.
    if points >= 10:  # Sprawdza, czy wynik jest w przedziale od 10 do 13 punktów.
        return 'Satisfactory'  # Zwraca ocenę dostateczną.
    return 'Fail'  # Zwraca informację o niezaliczeniu przy wyniku poniżej 10 punktów.


if __name__ == '__main__':  # Wykonuje przykład przy bezpośrednim uruchomieniu pliku.
    test_result = 15  # Ustala przykładową liczbę punktów.
    final_grade = pts_to_grade(test_result)  # Wyznacza ocenę dla przykładowego wyniku.
    print(f'You scored {test_result} points on the test. Your final grade is {final_grade}.')  # Wyświetla wynik i ocenę.
