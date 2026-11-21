# Zadanie 7.26. Rozdzielamy znaki napisu myślnikami.

def f(text):  # Przyjmuje tekst do przekształcenia.
    return '-'.join(text)  # Łączy kolejne znaki tekstu, wstawiając myślnik między każdą parę.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim otwarciu pliku.
    print(repr(f('Univesity')))  # Wypisuje rozdzielone znaki przykładowego słowa z apostrofami dzięki repr().
    print(repr(f('UE')))  # Wypisuje 'U-E'.
    print(repr(f('x')))  # Wypisuje 'x', bo pojedynczy znak nie wymaga separatora.
    print(repr(f('')))  # Wypisuje dwa apostrofy, żeby pusty wynik był widoczny.
