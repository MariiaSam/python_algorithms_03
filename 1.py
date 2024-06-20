'''
творіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.



Вимоги до завдання:



Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
Для роботи з датами слід використовувати модуль datetime Python.


Рекомендації для виконання:



Імпортуйте модуль datetime.
Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
Отримайте поточну дату, використовуючи datetime.today().
Розрахуйте різницю між поточною датою та заданою датою.
Поверніть різницю у днях як ціле число.

Критерії оцінювання:
Коректність роботи функції: функція повинна точно обраховувати кількість днів між датами.
Обробка винятків: функція має впоратися з неправильним форматом вхідних даних.
Читабельність коду: код повинен бути чистим і добре документованим.

'''
from datetime import datetime


def get_days_from_today(date):
    try:
        date_object = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.date.today()
        difference_between_days = current_date - date_object
        return difference_between_days.days
    except:
        return 'Invalid format'


print(get_days_from_today('2020-10-09'))
