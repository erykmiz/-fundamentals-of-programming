# Zadanie 6.4: odczytanie danych pracownika za pomocą wycinków tekstu.
# W zapisie [początek:koniec] początek należy do wycinka, a koniec już nie; pozycje liczymy od 0.
employee = "Mr. John May, born on 1998-02-16"  # Zapisuje opis pracownika podany w zadaniu.
print(f"Name: {employee[4:8]}")  # Pobiera znaki z pozycji 4, 5, 6 i 7, czyli John.
print(f"Surname: {employee[9:12]}")  # Pobiera znaki z pozycji od 9 do 11, czyli May.
print(f"Born: {employee[22:32]}")  # Pobiera znaki od pozycji 22 do 31, czyli datę 1998-02-16.
print(f"Initials: {employee[4]}{employee[9]}")  # Łączy pierwszą literę imienia i nazwiska: JM.
