
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def printCoordinatRange():
	print("Введите номер четверти: ")
	quort_number = int(input())

	if(quort_number == 1):
		print("x > 0, y > 0")
	if(quort_number == 2):
		print("x > 0, y < 0")
	if(quort_number == 3):
		print("x < 0, y < 0")
	if(quort_number == 4):
		print("x < 0, y > 0")

printCoordinatRange()



