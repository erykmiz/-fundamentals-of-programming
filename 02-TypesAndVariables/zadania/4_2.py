# Zadanie 4.2: obliczamy, ile dochodu rodziny przypada na jedną osobę.
# f wstawia wartości z {}; :.2f pokazuje 2 miejsca po kropce, bez zmiany wartości zmiennej.

father_income = 5450  # Zapamiętuje dochód ojca: 5450.
mother_income = 4920  # Zapamiętuje dochód matki: 4920.
family_members = 5  # Zapamiętuje, że dochód dzielimy między 5 członków rodziny.
total_income = father_income + mother_income  # Dodaje oba dochody: 5450 + 4920 = 10370.
income_per_person = total_income / family_members  # Dzieli 10370 przez 5, więc na osobę przypada 2074.

print(f"Total family income is {total_income:.2f}, and income per person is {income_per_person:.2f}")  # Pokazuje 10370.00 oraz 2074.00.
