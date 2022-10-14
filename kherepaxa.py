import turtle as t
import math

t.shape("turtle")
t.speed(0)

# настройка
walls_width = int(input("ширина стен: "))  # ширина стен
walls_height = int(input("высота стен: ")) # высота стен
walls_color = input("цвет стен (hex)")
roof_height = int(input("высота крыши: "))  # высота крыши
roof_color = input("цвет крыши (hex)")
roof_side = math.sqrt((walls_width / 2) ** 2 + roof_height ** 2)
roof_angle = math.degrees(math.atan(roof_height / (walls_width / 2)))

# нарисовать стены
t.fillcolor(walls_color)
t.begin_fill()
for i in range(2):
    t.fd(walls_width)
    t.left(90)
    t.fd(walls_height)
    t.left(90)
t.end_fill()

# нарисовать крышу
t.fillcolor(roof_color)
t.begin_fill()
t.left(roof_angle)
t.fd(roof_side)
t.right(roof_angle * 2)
t.fd(roof_side)
t.setheading(180) # посчитать
t.fd(walls_width)
t.end_fill()

t.done()
