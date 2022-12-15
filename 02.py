# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = 0
y = 1
z = 0

left = not (x or y or z)
right = not x and not y and not z
if left == right:
	print ("Утверждение инстино")
else:
	print ("Утверждение ложно")