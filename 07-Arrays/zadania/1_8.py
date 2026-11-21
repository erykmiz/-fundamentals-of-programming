# Zadanie 1.8. Sortujemy i numerujemy listę gier, korzystając z pętli while.

computer_games = [  # Zapisuje tytuły gier podane w zadaniu.
    'Minecraft', 'Fortnite', 'Cyberpunk 2077', 'The Witcher 3',  # Dodaje pierwsze cztery tytuły.
    'League of Legends', 'Valorant', 'Grand Theft Auto V',  # Dodaje kolejne trzy tytuły.
    'Elden Ring', 'Apex Legends', 'Call of Duty: Warzone',  # Dodaje trzy ostatnie tytuły.
]  # Kończy listę tytułów.

sorted_games = sorted(computer_games)  # Zwraca nową listę ułożoną alfabetycznie.
index = 0  # Ustawia początkowy indeks na pierwszy element posortowanej listy.
while index < len(sorted_games):  # Powtarza blok, dopóki indeks wskazuje istniejący tytuł.
    print(f'{index + 1}. {sorted_games[index]}')  # Numeruje gry od jedynki i pokazuje bieżący tytuł.
    index += 1  # Przechodzi do następnego indeksu listy.
