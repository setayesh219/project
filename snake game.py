import turtle
import time
import random
t = 0.1
score = 0
High_score = 0
#ايجاد صفحه بازي
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('lightBlue')
wn.setup(width=600 , height=600)
wn.tracer(0)
#سر مار
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("MistyRose4")
head.goto(0,0)
head.penup()
head.direction = "stop"
#غذاي مار
food = turtle.Turtle()
food.speed(0)
colors = random.choice(['black', 'orchid4', 'navy']) 
shapes = random.choice(['square', 'triangle', 'circle']) 
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0,100)
#بدن مار
segments = []
#امتياز بازي
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0 ,290)
pen.write("Score : 0   High Score : 0", align="center", font=("candara", 24, "bold"))
#تعريف توابع براي حرکت مار
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction== "up":
        y = head.ycor()
        head.sety( y + 20 )
    if head.direction== "down":
        y = head.ycor()
        head.sety( y - 20 )
    if head.direction== "left":
        x = head.xcor()
        head.setx( x - 20 )
    if head.direction== "right":
        x = head.xcor()
        head.setx( x + 20 )
#تعريف کليد ها براي کنترل مار 
wn.listen()
wn.onkeypress(go_up , "w")
wn.onkeypress(go_down , "s")
wn.onkeypress(go_left , "a")
wn.onkeypress(go_right , "d")

while True:
    wn.update()
    #بررسي برخورد مار با ديواره
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        #ريست شدن بازي
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()
        score = 0
        t = 0.1
        pen.clear()
        pen.write("Score : {}   High Score : {}".format(score, High_score), align="center", font=("candara", 24, "bold"))
    #جابجايي غذا
    if head.distance(food) < 20:
        x = random.randint(-290 , 290)
        y = random.randint(-290 , 290)
        food.goto(x,y)
        #افزايش طول بدن مار و سرعت
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green4")
        new_segment.penup()
        segments.append(new_segment)
        t -= 0.001
        #افزايش و به روزرساني امتياز بازي با خوردن غذا
        score += 10
        if score > High_score:
            High_score = score
        pen.clear()
        pen.write("Score : {}   High Score : {}".format(score, High_score), align="center", font=("candara", 24, "bold"))
    #حرکت بدن مار
    for indix in range(len(segments)-1,0,-1):
        #به دست اوردن موقعيت بخش قبلي بدن مار
        x = segments[indix-1].xcor()
        y = segments[indix-1].ycor()
        #انتقال بخش فعلي به موقعيت بخش قبلي
        segments[indix].goto(x,y)
    #اولين بخش مار به موقعيت سر مار منتقل ميشود
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)    
    move()
    #بررسي برخورد سر مار با بدن خودش
    for segment in segments:
        if segment.distance(head)<20:
            #ريست شدن بازي
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()
            score = 0
            t = 0.1
            pen.clear()
            pen.write("Score : {}   High Score : {}".format(score, High_score), align="center", font=("candara", 24, "bold"))
            
    time.sleep(t)

wn.mainloop()
