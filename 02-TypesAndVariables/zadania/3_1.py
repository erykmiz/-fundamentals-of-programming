# Zadanie 3.1: analiza siedmiu zmiennych, ich wartości i typów.

company = "ABC Data"  # Zmienna company przechowuje nazwę firmy; wartość: "ABC Data", typ: str.
phone = "555-123-009"  # Zmienna phone przechowuje numer telefonu jako tekst typu str.
employees = 25  # Zmienna employees przechowuje liczbę pracowników: 25, typ int.
remote_work = True  # Zmienna remote_work przechowuje wartość True typu bool.
big_company = employees > 100  # Sprawdza, czy pracowników jest ponad 100; wartość: False, typ: bool.
income = 4500000  # Zmienna income przechowuje dochód: 4500000, typ int.
income_per_person = income / employees  # Dzieli dochód przez liczbę pracowników; wartość: 180000.0, typ: float.

print("Liczba zmiennych w analizowanym programie: 7")  # Podaje łączną liczbę zmiennych z treści zadania.
print("company:", company, "| typ:", type(company))  # Wyświetla nazwę, wartość i typ zmiennej company.
print("phone:", phone, "| typ:", type(phone))  # Wyświetla nazwę, wartość i typ zmiennej phone.
print("employees:", employees, "| typ:", type(employees))  # Wyświetla nazwę, wartość i typ zmiennej employees.
print("remote_work:", remote_work, "| typ:", type(remote_work))  # Wyświetla nazwę, wartość i typ zmiennej remote_work.
print("big_company:", big_company, "| typ:", type(big_company))  # Wyświetla nazwę, wartość i typ zmiennej big_company.
print("income:", income, "| typ:", type(income))  # Wyświetla nazwę, wartość i typ zmiennej income.
print("income_per_person:", income_per_person, "| typ:", type(income_per_person))  # Wyświetla dochód na osobę i jego typ.
