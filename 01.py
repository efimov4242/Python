# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

def isWeekendDay():
	print("Введите день недели: ")
	dayNumber = int(input())

	while(dayNumber <= 0 or dayNumber > 7):
		print("Введите число от 0 до 7: ")
		dayNumber = int(input())

	if dayNumber > 0 and dayNumber <= 5:
		print ("Нет")
	if dayNumber > 5 and dayNumber <= 7:
		print ("Да")

isWeekendDay()