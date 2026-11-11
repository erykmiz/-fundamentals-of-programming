# Zadanie 6.5: rozdzielamy numer telefonu na trzy grupy po trzy cyfry.
# Wpisz 9 cyfr; [0:3] bierze pozycje 0, 1, 2, bez 3.
# f przed tekstem pozwala wstawić w miejsca {} wartości zmiennych lub wyniki działań.

phone = input("Enter phone number: ")  # Prosi o numer i zachowuje go jako tekst, także gdy zaczyna się od zera.

formatted_phone = phone[0:3] + "-" + phone[3:6] + "-" + phone[6:9]  # Dla 543097329 łączy 543, -, 097, -, 329.
print(f"Phone number: {formatted_phone}")  # print() pokazuje wynik; f wstawia w {} tekst, np. 543-097-329.
