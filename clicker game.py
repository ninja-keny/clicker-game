import turtle 
import time

shop2 = turtle.Turtle()
draw = turtle.Turtle()
shop = turtle.Turtle()
screen = turtle.Screen()
upgrade = turtle.Turtle()
upgrade2 = turtle.Turtle()
purchase = turtle.Turtle()
autoclick = turtle.Turtle()
color = turtle.Turtle()
back = turtle.Turtle()
setting_turtle = turtle.Turtle()
lightblue = turtle.Turtle()
lightblue.hideturtle()
green = turtle.Turtle()
run = True
turtle.hideturtle()
autoclick.hideturtle()

shop_on = False
click = 0
wait = 0
click_power = 1
swicth = 0
setting_on = False

def players_score():
    global score
    draw.clear()   
    draw.write("Score: " + str(score), font=("Arial", 16, "bold"))

#purchase
purchase.hideturtle()
purchase.penup()
purchase.goto(-100,150)
purchase.pendown()

# upgrade2
upgrade2.hideturtle()
upgrade2.penup()
upgrade2.goto(108,150)
upgrade2.pendown()
upgrade2.pensize(5)

#light blue
lightblue.penup()
lightblue.goto(-150,0)

#green
green.hideturtle()
green.penup()
green.goto(-80,0)

#color 
color.hideturtle()
color.speed(0)

#back
back.hideturtle()
back.speed(0)
back.penup()
back.goto(-175,150)
back.pendown()

#change auto clicker
extra = 0

def autoclicker():
    global extra, score
    score += extra

    # ALWAYS update score
    draw.clear()
    draw.write("Score: " + str(score), font=("Arial", 16, "bold"))

    screen.ontimer(autoclicker, 1000)

# setting
def setting_box():
    setting_turtle.hideturtle()
    setting_turtle.setheading(360)
    setting_turtle.speed(1000000000)
    setting_turtle.penup()
    setting_turtle.goto(-200,150)
    setting_turtle.begin_fill()
    for i in range(2):
        setting_turtle.pendown()
        setting_turtle.forward(90)
        setting_turtle.left(90)
        setting_turtle.forward(50)
        setting_turtle.left(90)
    setting_turtle.color("grey")
    setting_turtle.end_fill()
    setting_turtle.left(45)
    setting_turtle.forward(25)
    setting_turtle.color("black")
    setting_turtle.write("setting", font=("Arial", 13, "bold"))
 
setting_box()
    
# upgrade
upgrade.hideturtle()
upgrade.penup()
upgrade.speed(0)

# circle
def circle():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.hideturtle()
    turtle.color("blue")
    turtle.dot(50)
circle()

# shop 
def shop_drawing():
    shop.hideturtle()
    shop.setheading(360)
    shop.speed(0)
    shop.penup()
    shop.goto(100,150)
    shop.begin_fill()
    for i in range(2):
        shop.pendown()
        shop.forward(100)
        shop.left(90)
        shop.forward(50)
        shop.left(90)
    shop.color("orange")
    shop.end_fill()
    shop.left(45)
    shop.forward(25)
    shop.color("black")
    shop.write("shop", font=("Arial", 16, "bold"))
    shop.penup()
    shop.goto(150,175)

shop_drawing()
shop2.hideturtle()

score = 0
draw.speed(0)
draw.penup()
draw.goto(-100, 100)
draw.pendown()
draw.write("Score: 0", font=("Arial", 16, "bold"))
draw.hideturtle()

def clicked(x, y):
    global score
    global shop_on
    global click
    global wait
    global extra
    global swicth
    global setting_on
    global click_power

    # click circle
    if turtle.distance(x, y) < 25:
        score += click_power
        draw.clear()   
        draw.write("Score: " + str(score), font=("Arial", 16, "bold"))

    # BACK BUTTON
    if back.distance(x,y) < 60:
        if swicth == 1:
            if setting_on == True:
                setting_on = False
                swicth = swicth + 1
                back.clear()
                color.clear()
                back.penup()
                shop_drawing()
                setting_box()
                circle()
                players_score()
                lightblue.clear()
                green.clear()

    # SETTINGS BUTTON
    if setting_turtle.distance(x,y) < 60:
        if setting_on == False:
            if swicth == 0 :
                swicth = swicth + 1
                setting_on = True
                shop.clear()
                upgrade.clear()
                autoclick.clear()
                upgrade2.clear()
                setting_turtle.clear()
                draw.clear()
                turtle.clear()
                color.hideturtle()
                back.penup()
                back.goto(-190,150)
                color.penup()
                color.goto(-50,150)
                color.pendown()
                color.write("background color", font=("Arial", 14, "bold"))
                back.begin_fill()
                back.setheading(360)
                for i in range(2):
                    back.pendown()
                    back.forward(100)
                    back.left(90)
                    back.forward(50)
                    back.left(90)
                back.color("grey")
                back.end_fill()
                back.left(45)
                back.forward(25)
                back.color("black")
                back.write("back", font=("Arial", 16, "bold"))

                # lightblue
                lightblue.penup()
                lightblue.speed(1000)
                lightblue.hideturtle()
                lightblue.goto(-150,0)
                lightblue.pendown()
                lightblue.color("lightblue")
                lightblue.dot(50)
       
                #green
                green.color("green")
                green.dot(50)

    if lightblue.distance(x,y) < 20 and setting_on:
        screen.bgcolor("lightblue")
    
    if green.distance(x,y) < 20 and setting_on:
        screen.bgcolor("green")

    if swicth == 2:
        swicth = 0

    # SHOP BUTTON
    if shop.distance(x,y) < 70:
        if click == 2:
            click = 0
        else:  
            click += 1
        if click == 1:
            if shop_on == False:      
                shop.clear()
                shop.speed(10000000000000000000)
                shop_on = True
                wait = 1
                if click == 1:
                    click = 0
                else:  
                    click += 1

                # DRAW SHOP
                upgrade.clear()
                upgrade.penup()
                upgrade.goto(100,200)
                upgrade.pendown()
                upgrade.pensize(10)
                upgrade.begin_fill()
                upgrade.forward(99)
                upgrade.right(90)
                upgrade.forward(380)
                upgrade.right(90)
                upgrade.forward(99)
                upgrade.right(90)
                upgrade.forward(380)
                upgrade.color("grey")
                upgrade.end_fill()
      
                upgrade.right(90)
                upgrade.penup()
                upgrade.forward(5)
                upgrade.right(90)
                upgrade.forward(30)
                upgrade.pendown()
                upgrade.color("black")
                upgrade.write("shop",font=("arial",16,"bold"))
      
                upgrade.pensize(4)
                upgrade.penup()
                upgrade.forward(5)
                upgrade.pendown()
                upgrade.left(90)
                upgrade.forward(55)
                upgrade.penup()
                upgrade.forward(35)
                upgrade.pendown()
       
                for i in range (4):
                    upgrade.left(90)
                    upgrade.forward(35)
                upgrade.goto(155,200)
                upgrade.goto(200,200)
                upgrade.goto(163,165)
                upgrade.penup()
                upgrade.goto(185,175)
            
                upgrade2.goto(108,150)
                upgrade2.speed(10000000)
                upgrade2.begin_fill()
                upgrade2.color("black")
                upgrade2.pendown()
                for i in range(2):
                    upgrade2.forward(80)
                    upgrade2.right(90)
                    upgrade2.forward(40)
                    upgrade2.right(90)
                upgrade2.color("grey")
                upgrade2.end_fill()
                upgrade2.color("black")
                upgrade2.penup()
                upgrade2.goto(110,130)
                upgrade2.pendown()
                upgrade2.write("power click", font = ("Arial",10,"bold"))
                upgrade2.penup()
                upgrade2.goto(110,115)
                upgrade2.pendown()
                upgrade2.write("cost 10 clicks", font = ("Arial",8,"bold"))
                upgrade2.penup()
                upgrade2.goto(140,130)
          
                autoclick.hideturtle()
                autoclick.penup()
                autoclick.goto(107,90)
                autoclick.speed(0)
                autoclick.pensize(5)
                autoclick.pendown()
                for i in range(2):
                    autoclick.forward(80)
                    autoclick.right(90)
                    autoclick.forward(40)
                    autoclick.right(90)
                autoclick.penup()
                autoclick.goto(110,70)
                autoclick.pendown()
                autoclick.write("auto clicks", font = ("Arial",10,"bold"))
                autoclick.penup()
                autoclick.goto(110,60)
                autoclick.pendown()
                autoclick.write("cost 100 clicks", font = ("Arial",8,"bold"))
                autoclick.penup()
                autoclick.goto(150,70)

    # BUY AUTOCLICKER
    if autoclick.distance(x,y) < 40 and shop_on:
        if score > 99:
            score -= 100
            extra += 1
            autoclicker()   
        else:
            purchase.color("red")
            purchase.write("not enough clicks", font=("Arial",16,"bold"))
            time.sleep(0.5)
            purchase.clear()

    # BUY POWER CLICK
    if upgrade2.distance(x,y) < 40 and shop_on:
        if score > 9:
            score -= 10
            draw.clear()   
            draw.write("Score: " + str(score), font=("Arial", 16, "bold"))
            click_power += 1
        else:
            purchase.color("red")
            purchase.write("not enough clicks", font=("Arial",16,"bold"))
            time.sleep(0.5)
            purchase.clear()

    # EXIT SHOP
    if upgrade.distance(x,y) < 40:
        if click == 2:
            click = 0
        else:  
            click += 1
        if click == 2 or wait == 0:
            if shop_on == True:   
                upgrade.clear()
                upgrade2.clear()
                autoclick.clear()
                shop.goto(100,150)
                shop_drawing()
                shop_on = False
                return

screen.onscreenclick(clicked)
screen.mainloop()
