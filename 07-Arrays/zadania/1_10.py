# Zadanie 1.10. Obliczamy liczbę i odsetek poprawnych odpowiedzi w teście.

test_results = [  # Tworzy listę odpowiedzi oznaczonych wartościami True i False.
    False, True, False, True, True,  # Zapisuje wyniki pierwszych pięciu pytań.
    True, True, False, True, True,  # Zapisuje wyniki pytań od szóstego do dziesiątego.
    False, True, True, True, False,  # Zapisuje wyniki ostatnich pięciu pytań.
]  # Kończy listę wyników.

question_count = len(test_results)  # Liczy pytania, ponieważ każda odpowiedź zajmuje jedną pozycję.
correct_answers = 0  # Zaczyna zliczanie poprawnych odpowiedzi od zera.
for answer in test_results:  # Przechodzi po kolejnych odpowiedziach.
    if answer:  # Wykonuje wciętą instrukcję, gdy odpowiedź ma wartość True.
        correct_answers += 1  # Dolicza jedną poprawną odpowiedź.

incorrect_answers = question_count - correct_answers  # Odejmuje liczbę odpowiedzi poprawnych od wszystkich.
percentage = correct_answers / question_count * 100  # Zamienia udział poprawnych odpowiedzi na procent.

print('TEST STATISTICS')  # Wypisuje tytuł statystyk.
print('===============')  # Dodaje linię pod tytułem.
print('Number of questions:', question_count)  # Pokazuje liczbę wszystkich pytań.
print('Number of correct answers:', correct_answers)  # Pokazuje liczbę poprawnych odpowiedzi.
print('Number of incorrect answers:', incorrect_answers)  # Pokazuje liczbę błędnych odpowiedzi.
print(f'Percentage of correct answers: {percentage:.2f}%')  # Wyświetla procent z dwiema cyframi po kropce.
