# Zadanie 3.1: opisujemy siedem zmiennych z przykładowymi danymi firmy.

company = "ABC Data"  # Pod nazwą company zapisuje tekst ABC Data; cudzysłowy wskazują typ str.
phone = "555-123-009"  # Zapisuje numer jako tekst typu str; myślniki są częścią numeru, nie odejmowaniem.
employees = 25  # Pod nazwą employees zapisuje liczbę pracowników: 25; jej typ to int.
remote_work = True  # Zapisuje informację „tak, praca zdalna”; True znaczy prawda i ma typ bool.
big_company = employees > 100  # Najpierw pyta, czy 25 > 100; odpowiedź False zapisuje jako bool w big_company.
income = 4500000  # Zapisuje dochód 4 500 000 jako liczbę całkowitą typu int.
income_per_person = income / employees  # Dzieli 4500000 przez 25 osób; wynik 180000.0 ma typ float, bo użyto /.

print("Liczba zmiennych w analizowanym programie: 7")  # Pokazuje odpowiedź: w oryginalnym programie jest 7 zmiennych.
print("company:", company, "| typ:", type(company))  # Pokazuje podpis company, wartość ABC Data i jej typ str.
print("phone:", phone, "| typ:", type(phone))  # Pokazuje numer 555-123-009 oraz informację, że to tekst typu str.
print("employees:", employees, "| typ:", type(employees))  # Pokazuje liczbę pracowników 25 i typ int.
print("remote_work:", remote_work, "| typ:", type(remote_work))  # Pokazuje True, czyli prawdę, oraz typ bool.
print("big_company:", big_company, "| typ:", type(big_company))  # Pokazuje False, bo 25 nie jest większe od 100, oraz typ bool.
print("income:", income, "| typ:", type(income))  # Pokazuje dochód 4500000 i typ int.
print("income_per_person:", income_per_person, "| typ:", type(income_per_person))  # Pokazuje 180000.0 i typ float.
