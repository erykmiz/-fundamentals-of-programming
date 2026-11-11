# Zadanie 2.2: liczymy znaki działań, wartości użyte w działaniach i wynik każdego wyrażenia.
# Operator to znak działania lub porównania; argument to każde wystąpienie wartości.
# Najpierw **, potem *, / i %, a na końcu +; *, / i % liczymy tu od lewej.

print(3 * 2 + 1)  # 2 operatory (* i +), 3 argumenty (3, 2, 1); pokazuje 7.
print(5 + 10 * 5)  # 2 operatory (+ i *), 3 argumenty (5, 10, 5); pokazuje 55.
print(4 + 4 / 2 ** 2)  # 3 operatory (+, /, **), 4 argumenty (4, 4, 2, 2); wynik to 5.0.
print(4 % 3 % 2 % 1)  # 3 operatory (trzy znaki %), 4 argumenty (4, 3, 2, 1); wynik to 0.
print(1 + 2 % 3 ** 4 * 5)  # 4 operatory (+, %, **, *), 5 argumentów (1, 2, 3, 4, 5); wynik to 11.
print(True != False)  # 1 operator (!=), 2 argumenty (True, False); pokazuje True.
