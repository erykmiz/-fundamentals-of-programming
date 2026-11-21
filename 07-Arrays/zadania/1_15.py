# Zadanie 1.15. Sortujemy spalanie samochodu i transakcje metodą bąbelkową.
# Funkcja zmienia otrzymaną listę i zwraca ją po posortowaniu.

def bubble_sort(arr):  # Przyjmuje listę liczb do posortowania rosnąco.
    n = len(arr)  # Zapamiętuje długość listy.
    for i in range(n - 1):  # Wykonuje najwyżej n - 1 przejść dla listy o n elementach.
        for j in range(n - i - 1):  # Porównuje sąsiadów z pominięciem końca ułożonego we wcześniejszych przejściach.
            if arr[j] > arr[j + 1]:  # Sprawdza, czy sąsiednia para jest w złej kolejności.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Zamienia wartości tej pary miejscami.
    return arr  # Zwraca listę, w której liczby są ułożone od najmniejszej do największej.


if __name__ == '__main__':  # Uruchamia przykłady przy bezpośrednim starcie pliku.
    car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]  # Zapisuje pomiary spalania.
    print(car_fuel_consumption)  # Pokazuje dane przed sortowaniem.
    sorted_fuel_consumption = bubble_sort(car_fuel_consumption)  # Sortuje listę spalania i zapisuje zwróconą listę.
    print(sorted_fuel_consumption)  # Pokazuje spalanie w kolejności rosnącej.

    bank_transactions = [-150, -20, 300, -45, -60, 500, -120]  # Zapisuje kwoty transakcji bankowych.
    print(bank_transactions)  # Pokazuje dane przed sortowaniem.
    sorted_bank_transactions = bubble_sort(bank_transactions)  # Sortuje transakcje od najmniejszej kwoty.
    print(sorted_bank_transactions)  # Pokazuje posortowane kwoty transakcji.
