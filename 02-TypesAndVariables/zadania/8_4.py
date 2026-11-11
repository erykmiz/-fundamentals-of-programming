# Zadanie 8.4: zamieniamy 170 centymetrów na pełne stopy i pozostałe cale.
# 1 cal = 2.54 cm, a 1 stopa = 12 cali.
# f wstawia wartości z {}; :.2f pokazuje 2 miejsca po kropce, bez zmiany wartości zmiennej.

cm = 170  # Zapisuje przykładowy wzrost 170 cm; = oznacza zapisanie wartości w zmiennej cm.
total_inches = cm / 2.54  # Dzieli 170 przez długość jednego cala i otrzymuje około 66.9291 cala.
feet = int(total_inches // 12)  # // 12 liczy pełne stopy: 5.0; int zamienia 5.0 na 5.
inches = total_inches % 12  # % 12 liczy pozostałe cale: około 6.93.
print(f'I am {cm}cm tall, i.e. {feet} feet and {inches:.2f} inches')  # Pokazuje wynik przykładu: 170 cm to 5 stóp i około 6.93 cala.
