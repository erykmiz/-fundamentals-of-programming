# Zadanie 1.16. Sortujemy trzy kolekcje wbudowaną funkcją sorted.
# Opis funkcji https://docs.python.org/3/library/functions.html#sorted

distances_traveled = [120, 150, 180, 90, 200, 175, 160]  # Zapisuje przebyte odległości.
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]  # Zapisuje dzienne temperatury.
file_names = [  # Rozpoczyna listę nazw plików do posortowania.
    'report.docx', 'presentation.pptx', 'data.csv', 'photo.jpg', 'notes.txt',  # Zapisuje pierwsze pięć nazw.
    'invoice.pdf', 'resume.docx', 'budget.xlsx', 'meeting.mp4', 'schedule.pdf',  # Zapisuje pozostałe pięć nazw.
]  # Kończy listę nazw plików.

sorted_distances = sorted(distances_traveled)  # Układa odległości od najmniejszej do największej.
sorted_temperatures = sorted(daily_temperatures, reverse=True)  # Odwraca porządek, aby ułożyć temperatury malejąco.
sorted_file_names = sorted(file_names)  # Układa nazwy plików alfabetycznie.
print('Distances:', sorted_distances)  # Wyświetla posortowane odległości.
print('Temperatures:', sorted_temperatures)  # Wyświetla posortowane temperatury.
print('File names:', sorted_file_names)  # Wyświetla uporządkowane nazwy plików.
