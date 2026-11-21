# Zadanie 3.25. Liczymy słowa i pokazujemy je w dwóch porządkach.

import MyText  # Wczytuje funkcje do przetwarzania tekstu z sąsiedniego pliku MyText.py.

if __name__ == '__main__':  # Wykonuje analizę po bezpośrednim uruchomieniu pliku.
    text = 'An apple a day keeps the doctor away'  # Zapisuje tekst podany w zadaniu.
    print('Text:', text)  # Wyświetla pełny tekst.
    print('Number of words:', MyText.word_count(text))  # Wyświetla liczbę słów, czyli 8.
    longest_first = MyText.words_by_length(text)  # Pobiera słowa w kolejności od najdłuższych do najkrótszych.
    print('Words from the longest:', ','.join(longest_first))  # Łączy słowa przecinkami i wypisuje wynik.
    alphabetical = MyText.words_alphabetically(text)  # Pobiera słowa uporządkowane alfabetycznie.
    print('Words ordered alphabetically:', ','.join(alphabetical))  # Wyświetla słowa w porządku alfabetycznym.
