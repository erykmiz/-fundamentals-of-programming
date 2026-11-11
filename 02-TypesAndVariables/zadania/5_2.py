# Zadanie 5.2: z długości boku sześcianu liczymy objętość i pole wszystkich ścian.
# ** oznacza potęgowanie, a * mnożenie; 4 ** 3 to 4 * 4 * 4.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

cube_side_string = input("Enter cube side: ")  # Pyta o bok; po wpisaniu 4 input() oddaje tekst "4".
cube_side = int(cube_side_string)  # int() zamienia tekst "4" na liczbę całkowitą 4.
cube_volume = cube_side ** 3  # Dla boku 4 liczy 4 * 4 * 4 = 64 jednostki sześcienne.
cube_surface_area = 6 * cube_side ** 2  # Dla boku 4 liczy 6 * (4 * 4) = 96 jednostek kwadratowych.

print(f"The volume of a cube with side {cube_side} is {cube_volume}")  # Pokazuje bok i objętość; np. dla 4 otrzymasz 64.
print(f"The surface area of a cube with side {cube_side} is {cube_surface_area}")  # Pokazuje bok i całe pole; np. dla 4 otrzymasz 96.
