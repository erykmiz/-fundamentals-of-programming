# Zadanie 6.2: liczymy samogłoski pętlą while.
# Indeksy tekstu zaczynają się od 0; in sprawdza, czy znak znajduje się w podanym tekście.

text = "This is a sample text."  # Zapisuje tekst do sprawdzenia.
vowels = "aeiouAEIOU"  # Zapisuje małe i wielkie samogłoski angielskie.
vowel_count = 0  # Zaczyna liczenie samogłosek od 0.
index = 0  # Ustawia indeks pierwszego znaku na 0.
while index < len(text):  # Sprawdza znaki, dopóki indeks jest mniejszy od długości tekstu.
    char = text[index]  # Bierze znak z bieżącej pozycji tekstu.
    if char in vowels:  # Sprawdza, czy znak należy do tekstu vowels.
        vowel_count += 1  # Zwiększa liczbę samogłosek o 1.
    index += 1  # Przechodzi do następnego znaku.
print(f"The number of vowels in the text is: {vowel_count}")  # Wstawia wynik w {} i pokazuje liczbę 6.
