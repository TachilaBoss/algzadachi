#1) Нахождение дистанции между точек
# def distance(x1, y1, x2, y2):
#     return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#
# x1 = float(input("Введите x1: "))
# y1 = float(input("Введите y1: "))
# x2 = float(input("Введите x2: "))
# y2 = float(input("Введите y2: "))
#
# result = distance(x1, y1, x2, y2)
# print(f"Расстояние между точкой ({x1}, {y1}) и ({x2}, {y2}) равно {result:.2f}")
#2) Отрицательная степень
# a = int(input("Укажите положительное число (A):"))
# n = int(input("Укажите целое число (N):"))
#
# def power(a, n):
#     if n == 0:
#         return 1
#     elif n < 0:
#         return 1 / (a * power(a, -n - 1))
#     else:
#         return a * power(a, n - 1)
#
# result = power(a, n)
# print(f"{a}^{n} = {result}")
#3) Число Фибоначчи
# n = int(input("Укажите число: "))
# def fib(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
# result = fib(n)
# print(f"Число Фибоначчи под номером {n} равно {result}")
#4) Проверка високосный год или нет
# def is_year_leap(year):
#     if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False
#
# year = int(input("Укажите нужный год для проверки: "))
# leap = is_year_leap(year)
# if leap:
#     print(f"{year} - Високосный год!")
# else:
#     print(f"{year} - Не високосный год!")
#5) Квадрат
# side = int(input("Укажите длинну стороны квадрата: "))
# def square(side_length):
#     perimeter = 4 * side_length
#     plochad = side_length ** 2
#     diagonal = side_length * 2 ** 0.5  # Диагональ - это сторона, умноженная на квадратный корень
#
#     return perimeter, plochad, diagonal
#
# perimeter, area, diagonal = square(side)
# print(f"Периметр: {perimeter}, Площадь: {area}, Диагональ: {diagonal}")
#6) Времена года
# def season(month):
#     if 1 <= month <= 2 or month == 12:
#         return "Зима"
#     elif 3 <= month <= 5:
#         return "Весна"
#     elif 6 <= month <= 8:
#         return "Лето"
#     elif 9 <= month <= 11:
#         return "Осень"
#     else:
#         return "Неверный номер месяца"
#
# month = int(input("Укажите месяц: "))
# result = season(month)
# print(f"Время года для месяца {month}: {result}")
# 7) Банковский вклад
# def bank(a, years):
#     interest_rate = 0.10  # Процент годовых
#     result = a * (1 + interest_rate) ** years
#     return result
#
# a = int(input("Укажите сумму которую вы хотите внести: "))
# years = int(input("Укажите на сколько лет вы хотите внести вклад: "))
# result = bank(a, years)
# print(f"Сумма на счету после {years} лет: {result:.2f} рублей")
# 8) Простые числа
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# cheknumber = int(input("Введите число от 0 до 1000: "))
#
# if 0 <= cheknumber <= 1000:
#     result = is_prime(cheknumber)
#     print(f"Число {cheknumber} простое: {result}")
# else:
#     print("Число вне допустимого диапазона.")
# 9) Дата
def year_date(day, month, year):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

from datetime import date

day = int(input("Укажите день: "))
month = int(input("Укажите месяц: "))
year = int(input("Укажите год: "))

if year_date(day, month, year):
    print("Дата существует в календаре!.")
else:
    print("Дата не существует в календаре!.")