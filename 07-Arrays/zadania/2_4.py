# Zadanie 2.4. Wyświetlamy nazwy dni i posiłki z tygodniowego jadłospisu.

def weekday(n):  # Przyjmuje numer dnia od 1 do 7.
    weekdays = [  # Zapisuje nazwy dni w kolejności od poniedziałku do niedzieli.
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',  # Nazwy czterech pierwszych dni.
        'Friday', 'Saturday', 'Sunday',  # Nazwy trzech pozostałych dni.
    ]  # Zamyka listę nazw.
    return weekdays[n - 1]  # Odejmuje 1, bo indeksy listy zaczynają się od 0.


def day_meal_plan(meal_plan, day_number):  # Przyjmuje jadłospis i numer wybranego dnia.
    meals = meal_plan[day_number - 1]  # Pobiera wiersz z trzema posiłkami danego dnia.
    return ', '.join(meals)  # Łączy nazwy posiłków przecinkiem i spacją.


if __name__ == '__main__':  # Wyświetla jadłospis po bezpośrednim uruchomieniu pliku.
    meal_plan = [  # Zapisuje śniadanie, lunch i obiad w osobnym wierszu dla każdego dnia.
        ['Oatmeal', 'Grilled Chicken Salad', 'Spaghetti'],  # Posiłki poniedziałkowe.
        ['Pancakes', 'Sandwich', 'Steak'],  # Posiłki wtorkowe.
        ['Smoothie', 'Chicken Wrap', 'Salmon'],  # Posiłki środowe.
        ['Eggs', 'Pasta', 'Soup'],  # Posiłki czwartkowe.
        ['Toast', 'Burrito', 'Pizza'],  # Posiłki piątkowe.
        ['Cereal', 'Salad', 'Fish Tacos'],  # Posiłki sobotnie.
        ['Bagel', 'Rice and Beans', 'Stir-fry'],  # Posiłki niedzielne.
    ]  # Zamyka listę z planem na siedem dni.

    print('WEEKLY MEAL PLAN')  # Wyświetla tytuł jadłospisu.
    print('(Breakfast, Lunch, Dinner)')  # Wyjaśnia kolejność wypisywanych posiłków.
    print('==========================')  # Oddziela nagłówek od jadłospisu.
    for day_number in range(1, len(meal_plan) + 1):  # Przechodzi po numerach od 1 do 7 włącznie.
        day = weekday(day_number)  # Odczytuje nazwę bieżącego dnia.
        meals = day_meal_plan(meal_plan, day_number)  # Pobiera połączone nazwy posiłków tego dnia.
        print(f'{day}: {meals}')  # Wypisuje nazwę dnia i jego trzy posiłki.
