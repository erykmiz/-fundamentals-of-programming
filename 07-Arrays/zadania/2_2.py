# Zadanie 2.2. Wyświetlamy planszę do gry w kółko i krzyżyk.

tic_tac_toe_board = [  # Tworzy listę trzech wierszy planszy.
    ['X', 'O', 'X'],  # Zapisuje pola pierwszego wiersza.
    [' ', 'X', 'O'],  # Zapisuje drugi wiersz z pustym pierwszym polem.
    ['O', ' ', 'X'],  # Zapisuje trzeci wiersz z pustym środkowym polem.
]  # Zamyka listę wierszy.

for row in tic_tac_toe_board:  # Pobiera kolejny wiersz planszy.
    for cell in row:  # Pobiera kolejno po jednym polu tego wiersza.
        print(cell, end=' ')  # Wypisuje pole i spację bez przechodzenia do nowej linii.
    print()  # Przechodzi do nowej linii po wypisaniu wszystkich pól wiersza.
