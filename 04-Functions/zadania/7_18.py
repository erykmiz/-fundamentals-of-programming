# Zadanie 7.18. Usuwamy spacje ze zdania.

def f(sentence):  # Przyjmuje dowolny napis.
    return sentence.replace(' ', '')  # Zamienia każde wystąpienie spacji na pusty tekst.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim otwarciu pliku.
    print(f('integrated development environment'))  # Pokazuje pierwsze zdanie bez spacji.
    sentence = 'A programming language is a system of notation for writing computer programs'  # Zapisuje drugie zdanie z polecenia.
    print(f(sentence))  # Pokazuje drugie zdanie bez spacji.
