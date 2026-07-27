import pgzrun,os,time
os.environ["SDL_VIDEO_CENTERED"]="1"

WIDTH=1000
HEIGHT=800

#variables

time1=15

list=[]


#Rectangles
answer1=Rect(50,200,425,200)
answer2=Rect(550,200,425,200)
answer3=Rect(50,425,425,200)
answer4=Rect(550,425,425,200)
question=Rect(50,75,700,100)
timer=Rect(770,75,180,100)
moving=Rect(50,10,900,55)
skip=Rect(50,650,925,100)


def draw():
    screen.fill((100,100,100))
    screen.draw.filled_rect(answer1,"red")
    screen.draw.filled_rect(answer2,"blue")
    screen.draw.filled_rect(answer3,"yellow")
    screen.draw.filled_rect(answer4,"green")
    screen.draw.filled_rect(question,(255,60,255))
    screen.draw.filled_rect(timer,(5,60,255))
    screen.draw.filled_rect(moving,(5,0,5))
    screen.draw.filled_rect(skip,(255,255,255))

    screen.draw.textbox(("Quizmaster"),moving,color="white")
    screen.draw.textbox(("SKIP"),skip, color="black",shadow=(0.5,0.2), scolor="pink")
    screen.draw.textbox((str(time1)),timer, color="white")

def update():
    global time1
    moving.x+=4
    if moving.x>1000:
        moving.right=0


def timee():
    global time1
    if time1>0:
     time1=time1-1
    print(time1)


clock.schedule_interval(timee,1)












































































































pgzrun.go()