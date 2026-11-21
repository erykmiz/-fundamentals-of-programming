# Moduł do zadania 3.25. Zliczamy i porządkujemy słowa w tekście.

def word_count(text):  # Przyjmuje tekst zawierający słowa oddzielone białymi znakami.
    return len(text.split())  # Dzieli tekst na słowa i zwraca ich liczbę.


def words_by_length(text):  # Przyjmuje tekst do sortowania według długości słów.
    words = text.split()  # Tworzy listę słów w kolejności wystąpienia w tekście.
    return sorted(words, key=len, reverse=True)  # Sortuje od najdłuższych, zachowując kolejność słów o tej samej długości.


def words_alphabetically(text):  # Przyjmuje tekst do sortowania alfabetycznego.
    words = text.split()  # Rozdziela tekst na poszczególne słowa.
    return sorted(words, key=str.casefold)  # Porównuje słowa bez rozróżniania wielkości liter i zachowuje ich zapis.
