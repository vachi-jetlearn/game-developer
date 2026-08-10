import pgzrun,os,time,random
os.environ["SDL_VIDEO_CENTERED"]="1"

WIDTH=1000
HEIGHT=800

game_over=False


#variables

time1=15

points=0

list=[]

path=("/Users/vachigupta/coding/python game developer/questions.txt")

def readq():
   global list
   file=open(path,"r")
   for i in file:
      list.append(i)
   file.close()
   print(list)

def seperate():
   global questans, game_over
   if len(list)==0:
         game_over=True

   else:
      random.shuffle(list)
      question=list.pop(0)
      questans=question.split(",")
      print(questans)
      
   
      
      
   

readq()





questans=[]

seperate()
   

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
    screen.draw.textbox((questans[0]),question,color="white",)
    screen.draw.textbox((questans[1]),answer1,color="white",)
    screen.draw.textbox((questans[2]),answer2,color="white",)
    screen.draw.textbox((questans[3]),answer3,color="white",)
    screen.draw.textbox((questans[4]),answer4,color="white",)

    if game_over==True:
        screen.draw.filled_rect(skip,(255,255,255))
        screen.draw.textbox(("Total points:"+str(points)),skip,color="black",shadow=(0.5,0.2), scolor="pink")


def update():
    global time1
    moving.x+=4
    if moving.x>1000:
        moving.right=0


def timee():
    global questans, game_over
    global time1
    if time1>0:
     time1=time1-1
    if time1==0:
       game_over=True
       questans=["Game Over!","-","-","-","-"]
   
   

def on_mouse_down(pos):
   global questans, points,game_over
   if skip.collidepoint(pos):
      seperate()
      if game_over==True:
         questans=["Game Over!","-","-","-","-"]
   if answer1.collidepoint(pos):
      print("you clicked answer 1")
      if int(questans[5])==1:
         print("correct")
         points=points+1
         print(points)
         seperate()
      else:
         seperate()

   elif answer2.collidepoint(pos):
         print("you clicked answer 2")
         if int(questans[5])==2:
            print("correct")
            
            points=points+1
            print(points)
            seperate()
         else:
            seperate()

   elif answer3.collidepoint(pos):
            print("you clicked answer 3")
            if int(questans[5])==3:
               print("correct")
               points=points+1
               print(points)
               seperate()
            else:
               seperate()

   elif answer4.collidepoint(pos):
            print("you clicked answer 4")
            if int(questans[5])==4:
               print("correct")
               points=points+1
               print(points)
               seperate()
            else:
               seperate()

            if game_over==True:
             questans=["Game Over!","-","-","-","-","-"]


if time1==0:
       game_over=True
if game_over==True:
            questans=["Game Over!","-","-","-","-","-"]
            

   


   
      

clock.schedule_interval(timee,1)












































































































pgzrun.go()