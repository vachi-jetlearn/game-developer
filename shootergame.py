import pgzrun, random, time

WIDTH=500
HEIGHT=500

goose=Actor("goo")
mes=""
col=True

def draw():
 global col
 screen.fill((255,0,43))
 
 
 if col==True:
    goose.draw()
 else:
    time.sleep(1)
    col=True

 screen.draw.text(mes,center=(250,50),fontsize=24)

def on_mouse_down(pos):
    global mes
    global col
    if goose.collidepoint(pos):
        mes="HOW DARE YOU SHOOT A GOOSE. IT IS MORE POWERFUL"
        #time.sleep(3)
        x=random.randint(0,500)
        y=random.randint(0,500)
        goose.x=x
        goose.y=y
        col=False
        
    else:
        mes="GOOD JOB. YOU HAVE TERRIBLE AIM"
        
        






















pgzrun.go()