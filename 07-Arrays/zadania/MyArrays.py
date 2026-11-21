# Moduł do zadania 3.20. Operacje na liście liczb.
# Drugą największą liczbę rozumiemy jako największą wartość mniejszą od maksimum.

def second_largest(array):  # Przyjmuje listę, w której szukamy drugiej największej wartości.
    if not array:  # Sprawdza, czy lista jest pusta.
        raise ValueError('The array is empty.')  # Zgłasza błąd, bo brakuje liczb do porównania.
    largest = array[0]  # Zaczyna od pierwszej liczby jako bieżącego maksimum.
    second = None  # Oznacza brak drugiej największej wartości na początku.
    for number in array[1:]:  # Sprawdza kolejne liczby, zaczynając od drugiej pozycji.
        if number > largest:  # Rozpoznaje nowe maksimum.
            second = largest  # Przenosi dotychczasowe maksimum na drugie miejsce.
            largest = number  # Zapamiętuje nową największą wartość.
        elif number < largest and (second is None or number > second):  # Szuka lepszego wyniku mniejszego od maksimum.
            second = number  # Zapamiętuje nową drugą największą wartość.
    if second is None:  # Sprawdza, czy znaleziono dwie różne liczby.
        raise ValueError('The array needs at least two different numbers.')  # Zgłasza błąd, gdy wszystkie wartości są takie same.
    return second  # Zwraca drugą największą wartość.


def smallest_largest(array):  # Przyjmuje listę i szuka jej dwóch wartości skrajnych.
    if not array:  # Sprawdza, czy w liście jest przynajmniej jedna liczba.
        raise ValueError('The array is empty.')  # Zgłasza błąd dla pustej listy.
    smallest = array[0]  # Zapamiętuje pierwszą liczbę jako początkowe minimum.
    largest = array[0]  # Zapamiętuje tę samą liczbę jako początkowe maksimum.
    for number in array[1:]:  # Przegląda pozostałe liczby.
        if number < smallest:  # Sprawdza, czy liczba jest mniejsza od bieżącego minimum.
            smallest = number  # Aktualizuje minimum.
        if number > largest:  # Sprawdza, czy liczba jest większa od bieżącego maksimum.
            largest = number  # Aktualizuje maksimum.
    return [smallest, largest]  # Zwraca dwuelementową listę z minimum i maksimum.


def range_difference(array):  # Przyjmuje listę do obliczenia rozstępu.
    smallest, largest = smallest_largest(array)  # Odczytuje obie wartości skrajne z listy zwróconej przez funkcję.
    return largest - smallest  # Odejmuje minimum od maksimum.


def median(array):  # Przyjmuje niepustą listę i wyznacza medianę bez funkcji wbudowanych.
    ordered = []  # Tworzy nową listę, aby zachować kolejność elementów podanego argumentu.
    count = 0  # Przechowuje liczbę elementów, które już wstawiono.
    for number in array:  # Przetwarza kolejne liczby z wejściowej listy.
        ordered.append(number)  # Dopisuje liczbę na końcu uporządkowanej części.
        position = count  # Zapamiętuje indeks właśnie dopisanej liczby.
        while position > 0 and ordered[position - 1] > number:  # Sprawdza, czy sąsiad po lewej jest większy.
            ordered[position] = ordered[position - 1]  # Przesuwa większego sąsiada o jedno miejsce w prawo.
            position -= 1  # Przechodzi w lewo w poszukiwaniu miejsca do wstawienia.
        ordered[position] = number  # Wstawia liczbę we właściwe miejsce w rosnącej kolejności.
        count += 1  # Zwiększa liczbę uporządkowanych elementów.
    if count == 0:  # Sprawdza, czy podana lista nie zawiera liczb.
        raise ValueError('The array is empty.')  # Zgłasza błąd, bo dla pustej listy nie ma mediany.
    middle = count // 2  # Wyznacza indeks środkowy przez dzielenie całkowite.
    if count % 2 == 1:  # Rozpoznaje nieparzystą liczbę elementów.
        return ordered[middle]  # Zwraca jedną liczbę znajdującą się pośrodku.
    return (ordered[middle - 1] + ordered[middle]) / 2  # Zwraca średnią dwóch środkowych liczb.


def numbers_to_string(array):  # Przyjmuje listę liczb w kolejności do zachowania.
    result = ''  # Przygotowuje pusty napis.
    for number in array:  # Przechodzi przez kolejne liczby.
        if result:  # Sprawdza, czy w napisie jest już poprzednia liczba.
            result += '-'  # Wstawia separator przed kolejną liczbą.
        result += str(number)  # Zamienia bieżącą liczbę na tekst i dopisuje ją do wyniku.
    return result  # Zwraca wszystkie liczby połączone myślnikami.
