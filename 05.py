# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def printDistance(ax, bx, ay, by):
	a_catet = ax - bx
	b_catet = ay - by
	hypotenuse = a_catet * a_catet + b_catet * b_catet
	print(round(hypotenuse ** (0.5), 3))


printDistance(3, 2, 6, 1)
