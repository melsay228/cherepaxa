import turtle as t
import math

t.shape("turtle")
t.speed(0)

# настройка
walls_widht = 200  # ширина стен
walls_geight = 100 # высота стен
roof_height = 150  # высота крыши
roof_side = math.sqrt((walls_wight / 2) ** 2 + roof_height ** 2)
print(roof_side)

for i in ramge(2):
    t.forward(walls_widht)
    t.left(90)
    t.forward(walls_height)
    t.left(90)

t.done()

FIXMI("картинка исчезает кза секунду ")