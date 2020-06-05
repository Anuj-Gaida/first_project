#simple snake game in python 
#by Anuj Gaida

import turtle
import time
import random

delay = 0.2

#score
score = 0
high_score = 0

#set up the screen
wn = turtle.Screen()
wn.title("Beat my score")
wn.bgcolor("black")
wn.setup(width = 600,height =600)
wn.tracer(0) #turns off the animation on the screen


# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("yellow")
head.penup() #to stop drawing lines
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup() #to stop drawing lines
food.goto(0,100)

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0 ,260)
pen.write("Score = 0  High Score = 0 " ,align="center" ,font=("courier" ,24,"normal"))




#functions
def go_up():
    head.direction ="up"

def go_down():
    head.direction ="down"

def go_right():
    head.direction ="right"

def go_left():
    head.direction ="left"            
    
def move():
    if head.direction == "up":
         y = head.ycor() #current y pos
         head.sety(y + 20)
    
    if head.direction == "down":
         y = head.ycor() #current y pos
         head.sety(y - 20)


    if head.direction == "right":
         x = head.xcor() #current x pos
         head.setx(x + 20)

    if head.direction == "left":
         x = head.xcor() #current x pos
         head.setx(x - 20)


#keybords binidings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")



# main game loop
while True:
    wn.update()
    #check for collision
    if head.xcor() > 290 or head.xcor()<-290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        # hide segments
        for i in segments:
            i.goto(1000,1000)

        #clear the segment list
        segments.clear()    
           
        #reset the score
        score = 0    
        #reset the delay 
        delay = 0.1

        pen.clear()
        pen.write("Score = {} High Score = {}" .format(score,high_score),align="center" ,font=("courier" ,24,"normal")  )    



 



    #check for collision with food
    if head.distance(food) < 20:
        #move food to random spot
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x , y)

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()#doesnot draw on the screen 
        segments.append(new_segment)
        

        #shorten the delay
        delay -= 0.001

        #increase score
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score = {} High Score = {}" .format(score,high_score),align="center" ,font=("courier" ,24,"normal")  )    
    #move end segment first 
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y) #newly added segments are send to the index of previous segments

    #move the segment  0 to where the head is 
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)    
 
    move() 
    
    #check for head collision with body
    for i in segments:
        if i.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            # hide segments
            for i in segments:
                i.goto(1000,1000)

             #clear the segment list
            segments.clear()  
            
            #reset the score
            score = 0
            #reset the delay 
            delay = 0.1

            #update the score display
            pen.clear()
            pen.write("Score = {} High Score = {}" .format(score,high_score),align="center" ,font=("courier" ,24,"normal")  )    

    time.sleep(delay)

wn.mainloop()
