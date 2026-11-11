# Zadanie 5.3: pobieranie imienia aż do podania niepustego tekstu.
name = ""  # Zapisuje pusty tekst, aby warunek pierwszego wejścia do pętli był prawdziwy.
while name == "":  # Ponawia pytanie, dopóki zmienna name zawiera pusty tekst.
    name = input("Enter your name: ").strip()  # Wczytuje imię i usuwa skrajne spacje; same spacje też nie wystarczą.
print(f"Hello {name}")  # Wyświetla powitanie z imieniem po opuszczeniu pętli.
