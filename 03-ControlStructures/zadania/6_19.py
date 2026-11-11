# Zadanie 6.19: ankieta z trzema odpowiedziami logicznymi.
print('SURVEY')  # Wyświetla tytuł ankiety.
computer_science = input('Are you interested in computer science? (y/n): ').strip().lower() == 'y'  # Zapisuje True dla odpowiedzi y i False dla n.
computer_games = input('Do you like playing computer games? (y/n): ').strip().lower() == 'y'  # Zamienia odpowiedź o grach na wartość logiczną.
instagram = input('Do you have an Instagram account? (y/n): ').strip().lower() == 'y'  # Zamienia odpowiedź o koncie na wartość logiczną.
print('SURVEY RESULTS')  # Wyświetla nagłówek wyników.
print(f"Interested in computer science: {'Yes' if computer_science else 'No'}")  # Wyświetla Yes dla True albo No dla False.
print(f"Playing computer games: {'Yes' if computer_games else 'No'}")  # Pokazuje odpowiedź na pytanie o gry jako słowo.
print(f"Has an Instagram account: {'Yes' if instagram else 'No'}")  # Pokazuje odpowiedź na pytanie o Instagram jako słowo.
