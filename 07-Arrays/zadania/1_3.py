# Zadanie 1.3. Porównujemy listę Pythona z tablicą z modułu array.
# Lista w Pythonie może przechowywać różne typy. Tablica array ma określony typ elementów.
# Zapis liczb jednego typu w tablicy pozwala ograniczyć zajmowaną pamięć.
# W kolejnych zadaniach używamy zwykłych list do reprezentowania tablic.

from array import array  # Udostępnia typ tablicy z biblioteki standardowej.

mixed_values = [2, 'tekst', 3.5]  # Tworzy listę z liczbą całkowitą, napisem i liczbą zmiennoprzecinkową.
integer_values = array('i', [2, 3, 7])  # Tworzy tablicę liczb całkowitych, co oznacza kod typu i.
print('List:', mixed_values)  # Pokazuje listę, której elementy mają różne typy.
print('Array:', integer_values)  # Pokazuje tablicę zawierającą liczby całkowite.
