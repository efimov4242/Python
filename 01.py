# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

print("Введите день недели: ")
week_day = int(input())
while(week_day <= 0 or week_day > 7):
	print("Введите число от 0 до 7: ")
	week_day = int(input())
if week_day > 0 and week_day <= 5:
	print("Нет")
if week_day > 5 and week_day <= 7:
	print("Да")
