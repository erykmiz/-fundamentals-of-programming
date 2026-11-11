# Zadanie 2.2: liczba operatorów, liczba argumentów i wartości wyrażeń.
# Argumenty oznaczają tutaj wystąpienia liczb lub wartości logicznych w danym wyrażeniu.
# Liczymy operatory wewnątrz wyrażeń, bez otaczającego je wywołania print().

print(3 * 2 + 1)  # 2 operatory (*, +), 3 argumenty (3, 2, 1); najpierw mnożenie, wynik: 7.
print(5 + 10 * 5)  # 2 operatory (+, *), 3 argumenty (5, 10, 5); najpierw 10 * 5, wynik: 55.
print(4 + 4 / 2 ** 2)  # 3 operatory (+, /, **), 4 argumenty; kolejno potęga, dzielenie, dodawanie: 5.0.
print(4 % 3 % 2 % 1)  # 3 operatory %, 4 argumenty; liczymy od lewej: 1 % 2 % 1, wynik: 0.
print(1 + 2 % 3 ** 4 * 5)  # 4 operatory (+, %, **, *), 5 argumentów; 1 + (2 % 81) * 5 daje 11.
print(True != False)  # 1 operator (!=), 2 argumenty (True, False); wartości są różne, wynik: True.
