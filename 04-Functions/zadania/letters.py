# Moduł do zadania 7.4. Liczymy wystąpienia wskazanej litery w dowolnym tekście.


def count_letter(text, letter):  # Przyjmuje tekst oraz pojedynczy znak do zliczenia.
    count = 0  # Ustawia początkowy licznik wystąpień na 0.
    for character in text:  # Przechodzi po kolejnych znakach tekstu.
        if character == letter:  # Porównuje znak z literą, uwzględniając wielkość liter.
            count += 1  # Zwiększa licznik o 1 po dopasowaniu.
    return count  # Zwraca łączną liczbę dopasowań po przejrzeniu tekstu.
