# Zadanie 5.3: liczymy objętość i pole pudełka o trzech wymiarach a, b i c.
# W poleceniu jest pomyłka: dla boków 3, 4, 5 objętość to 60, a pole 94.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

a = float(input("a="))  # Pyta o pierwszy bok, zmienia odpowiedź na liczbę i zapisuje ją w a.
b = float(input("b="))  # Tak samo pobiera drugi bok i zapisuje go w b.
c = float(input("c="))  # Tak samo pobiera trzeci bok i zapisuje go w c.
volume = a * b * c  # Mnoży trzy boki; np. 3 * 4 * 5 daje objętość 60.
surface_area = 2 * (a * b + a * c + b * c)  # Liczy 2 * (12 + 15 + 20) = 94; mnoży przez 2, bo każda ściana ma parę.

print(f"The volume of the cuboid is {volume}")  # Pokazuje objętość; dla boków 3, 4, 5 wyświetli 60.0.
print(f"The surface area of the cuboid is {surface_area}")  # Pokazuje całe pole; dla tych samych boków wyświetli 94.0.
