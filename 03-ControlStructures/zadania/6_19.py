# Zadanie 6.19: Zbieramy trzy odpowiedzi w ankiecie.
# strip().lower() usuwa skrajne spacje i zmienia litery na małe; porównanie z y daje True lub False.
# 'Yes' if warunek else 'No' wybiera Yes dla prawdy, a No dla fałszu.

print('SURVEY')  # Pokazuje tytuł ankiety.
computer_science = input('Are you interested in computer science? (y/n): ').strip().lower() == 'y'  # Pyta o informatykę i zapisuje odpowiedź jako True lub False.
computer_games = input('Do you like playing computer games? (y/n): ').strip().lower() == 'y'  # Pyta o gry i zapisuje odpowiedź jako True lub False.
instagram = input('Do you have an Instagram account? (y/n): ').strip().lower() == 'y'  # Pyta o Instagram i zapisuje odpowiedź jako True lub False.
print('SURVEY RESULTS')  # Pokazuje nagłówek wyników.
print(f"Interested in computer science: {'Yes' if computer_science else 'No'}")  # Pokazuje odpowiedź o informatyce jako Yes albo No.
print(f"Playing computer games: {'Yes' if computer_games else 'No'}")  # Pokazuje odpowiedź o grach jako Yes albo No.
print(f"Has an Instagram account: {'Yes' if instagram else 'No'}")  # Pokazuje odpowiedź o Instagramie jako Yes albo No.
