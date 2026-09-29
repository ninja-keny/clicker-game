import turtle 
import random
import time

rebirth = turtle.Turtle()
buy_all = turtle.Turtle()
text = turtle.Turtle()
fortune_circle = turtle.Turtle()
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

loading = False
rebirth_need = 1000000000
shop_on = False
click = 0
wait = 0
click_power = 1
already_click = False
swicth = 0
setting_on = False
color_chose = 0
fortune_circle.speed(0)
color_fortune = ["blue", "yellow", "ornage", "green", "red", "purple","pink","voilet"]
def players_score():
    global score
    draw.clear()   
    draw.write("Score: " + str(score), font=("Arial", 16, "bold"))
    
def change_color():
  global color_chose
  if color_chose == 8:
    color_chose = 0
  if setting_on == False:
   fortune_circle.color(color_fortune[color_chose])
   fortune_circle.dot(50)
   color_chose+=1
  screen.ontimer(change_color,1000)
  
#fortune circle
fortune_circle.hideturtle()
fortune_circle.penup()
fortune_circle.goto(60,-180)
change_color()

#enlarge
def big_circle():
 turtle.clear()
 turtle.dot(50)
  
#rebirth
rebirth.hideturtle()
rebirth.penup()
rebirth.speed(0)
def rebirth_box():
  rebirth.goto(-50,200)
  rebirth.color("black")
  rebirth.begin_fill()
  rebirth.pendown()
  for i in range(2):
   rebirth.forward(100)
   rebirth.right(90)
   rebirth.forward(50)
   rebirth.right(90)
  rebirth.color("yellow")
  rebirth.end_fill()
  rebirth.penup()
  rebirth.goto(-40,180)
  rebirth.color("black")
  rebirth.write("rebirth",font=("Arial",15, "bold"))



#text for fortue circle
text.hideturtle()
text.speed(0)
text.penup()

def text_circle():
 text.goto(43,-180)
 text.write("fortune",font=("Arial",7, "bold"))
 text.goto(47,-190)
 text.write("wheel",font=("Arial",7,"bold"))
text_circle()
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

#buy all button
buy_all.penup()
buy_all.hideturtle()
buy_all.pensize(5)
buy_all.goto(108,200)

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
    global already_click
    global loading
    # click circle
    if turtle.distance(x, y) < 25:
       score += click_power
       turtle.dot(70)
       big_circle()
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
                text_circle()
                fortune_circle.dot(50)

    # SETTINGS BUTTON
    if setting_turtle.distance(x,y) < 60:
        if setting_on == False:
            if swicth == 0 :
                swicth = swicth + 1
                setting_on = True
                fortune_circle.clear()
                shop.clear()
                upgrade.clear()
                buy_all.clear()
                autoclick.clear()
                upgrade2.clear()
                setting_turtle.clear()
                text.clear()
                draw.clear()
                turtle.clear()
                color.hideturtle()
                shop_on = False
                click = 0
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
    
    if fortune_circle.distance(x,y) < 50 and setting_on == False:
      addorsub = random.randint(1,3)
      try:
       if score >= 0:
        if addorsub == 1:
          score -= random.randint(0,score)
        elif addorsub == 2 or addorsub == 3:
          score += random.randint(0,score)
        players_score()
      except: 
         pass
        
    if green.distance(x,y) < 20 and setting_on:
        screen.bgcolor("green")

    if swicth == 2:
        swicth = 0


    # BUY AUTOCLICKER
    if autoclick.distance(x,y) < 40 and shop_on:
        if score > 99:
            score -= 100
            extra += 1
            if already_click == False:
             already_click = True
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
            
    if buy_all.distance(x,y) < 40 and shop_on:
      while score > 99:
        score = score - 100
        extra +=1
        if already_click == False:
          already_click = True
          autoclicker()
      if score > 9:
       while score > 9:
        score -= 10
        draw.clear()   
        draw.write("Score: " + str(score), font=("Arial", 16, "bold"))
        click_power += 1
      else:
        purchase.color("red")
        purchase.write("not enough clicks", font=("Arial",16,"bold"))
        time.sleep(0.5)
        purchase.clear()
        
   #shop
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
                loading = True
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
                
                buy_all.goto(108,30)
                buy_all.speed(10000000)
                buy_all.begin_fill()
                buy_all.color("black")
                buy_all.pendown()
                for i in range(2):
                    buy_all.forward(80)
                    buy_all.right(90)
                    buy_all.forward(40)
                    buy_all.right(90)
                buy_all.color("grey")
                buy_all.end_fill()
                buy_all.color("black")
                buy_all.penup()
                buy_all.goto(110,10)
                buy_all.pendown()
                buy_all.write("buy all upgrades", font = ("Arial",7,"bold"))
                buy_all.penup()
                buy_all.goto(110,0)
                buy_all.pendown()
                buy_all.write("need more that 10 clicks", font = ("Arial",5,"bold"))
                buy_all.penup()
                buy_all.goto(140,10)
          
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
                autoclick.goto(150,60)
                loading = False
    # EXIT SHOP
    if upgrade.distance(x,y) < 40:
      if loading == False:
        if click == 2:
            click = 0
        else:  
            click += 1
        if click == 2 or wait == 0:
            if shop_on == True:   
                upgrade.clear()
                upgrade2.clear()
                autoclick.clear()
                buy_all.clear()
                shop.goto(100,150)
                shop_drawing()
                shop_on = False
                return

screen.onscreenclick(clicked)
screen.mainloop()
