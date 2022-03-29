# 사각형 만들기
import turtle

for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
    
turtle.exitonclick()

# 삼각형 만들기
import turtle

for i in range(0,3):
    turtle.forward(100)
    turtle.right(360/3)

turtle.exitonclick()

# 원 그리기
import turtle

for i in range(36):
    turtle.forward(10)
    turtle.right(10)
    
turtle.exitonclick()

# 서로 붙어있지 않은 세개의 정사각형을 그려라
import turtle

turtle.color("black","red")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)
turtle.penup()
turtle.end_fill()

turtle.forward(200)
turtle.pendown()
turtle.color("black","blue")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)
turtle.penup()
turtle.end_fill()

turtle.right(90)
turtle.forward(200)
turtle.pendown()
turtle.color("black","green")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()

turtle.exitonclick()
    
# 별모양 그리기
import turtle

for i in range(5):
    turtle.right(144)
    turtle.forward(100)
    
turtle.exitonclick()

# 숫자 1의 밑에서부터 그리기 시작하여 다음의 그림처럼 숫자를 그려라
import turtle

turtle.left(90)
turtle.forward(100)
turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(180)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)

turtle.exitonclick()

# 각 선 색상을 다르게 하여(여섯개의 색상 목록에서 무작위로 선택하여)팔각형을 그려라
from random import random
import turtle

num = int(random()*6)+1
if num == 1:
    turtle.color("black","white")
elif num == 2:
    turtle.color("blue","white")
elif num == 3:
    turtle.color("green","white")
elif num == 4:
    turtle.color("yellow","white")
elif num == 5:
    turtle.color("red","white")
else:
    turtle.color("orange","white")
turtle.begin_fill()
for i in range(8):
    turtle.forward(100)
    turtle.right(360/8)
turtle.end_fill()

turtle.exitonclick()

# 67 패턴 만들기
import turtle

for i in range(0,10):
    turtle.right(36)
    for j in range(0, 8):
        turtle.forward(100)
        turtle.right(360/8)
        
turtle.exitonclick()

# 68 프로그램이 시작할 때마다 변경되는 패턴 그리기
from random import random
import turtle

line_num = int(random()*100)+1
line_len = int(random()*100)+1
angle_num = int(random()*180)+1

for i in range(line_num):
    turtle.forward(line_len)
    turtle.right(angle_num)
    
turtle.exitonclick()
