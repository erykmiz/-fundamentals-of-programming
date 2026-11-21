# Zadanie 7.22. Tworzymy skrót z pierwszych liter słów i zachowujemy ich wielkość.

def f(name):  # Przyjmuje tekst z dowolną liczbą słów.
    acronym = ''  # Zaczyna od pustego skrótu.
    for word in name.split():  # Przechodzi po słowach uzyskanych przez podział tekstu na białych znakach.
        acronym += word[0]  # Dopisuje pierwszy znak słowa, który ma indeks 0.
    return acronym  # Zwraca skrót złożony z zebranych liter.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim otwarciu pliku.
    print(f('Internet of Things'))  # Wypisuje IoT, zachowując małą literę o.
    print(f('For Your Information'))  # Wypisuje FYI.
    print(f('Python'))  # Wypisuje P dla jednego słowa.
