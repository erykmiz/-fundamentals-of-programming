# Zadanie 5.2: objętość i pole powierzchni sześcianu.
# Sprawdź bok 4: objętość 64, pole 96; bok 7: objętość 343, pole 294.
cube_side_string = input("Enter cube side: ")  # Pobiera bok z klawiatury; input zwraca tekst.
cube_side = int(cube_side_string)  # Zamienia tekst na liczbę całkowitą, aby można było liczyć.
cube_volume = cube_side ** 3  # Liczy objętość: bok razy bok razy bok.
cube_surface_area = 6 * cube_side ** 2  # Liczy pole sześciu kwadratowych ścian sześcianu.
print(f"The volume of a cube with side {cube_side} is {cube_volume}")  # Wyświetla długość boku i objętość.
print(f"The surface area of a cube with side {cube_side} is {cube_surface_area}")  # Wyświetla długość boku i całkowite pole powierzchni.
