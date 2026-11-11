# Zadanie 6.2: liczenie samogłosek za pomocą while zamiast for.
text = "This is a sample text."  # Zapisuje przykładowy tekst z programu vowels.py.
vowels = "aeiouAEIOU"  # Zapisuje samogłoski angielskie, uwzględniając małe i wielkie litery.
vowel_count = 0  # Przygotowuje licznik znalezionych samogłosek.
index = 0  # Zaczyna od pierwszego znaku tekstu, którego indeks wynosi zero.
while index < len(text):  # Powtarza sprawdzanie, dopóki indeks wskazuje istniejący znak tekstu.
    char = text[index]  # Odczytuje znak znajdujący się pod aktualnym indeksem.
    if char in vowels:  # Sprawdza, czy odczytany znak jest jedną z zapisanych samogłosek.
        vowel_count += 1  # Zwiększa licznik o jeden, gdy znaleziono samogłoskę.
    index += 1  # Przesuwa indeks do następnego znaku i pozwala pętli ostatecznie się zakończyć.
print(f"The number of vowels in the text is: {vowel_count}")  # Wyświetla wynik: 6 samogłosek.
