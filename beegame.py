import pgzrun, time, random

gameover=False

WIDTH=500
HEIGHT=500

bee=Actor("bee")
x=random.randint(0,500)
y=random.randint(0,500)
bee.pos=x,y
flower=Actor("flower")
x1=random.randint(0,500)
y1=random.randint(0,500)
flower.pos=x1,y1

score=0
def draw():
    if gameover==False:
        screen.blit("fieldd",(0,0))
        
        bee.draw()
        
        
        
        flower.draw()
        
        mes=("score: "+str(score))
        screen.draw.text(mes, center=(25,20),fontsize=20)
    else:
        screen.fill((255,44,33))
        mes=("score= "+str(score))
        screen.draw.text(mes, center=(250,250),fontsize=40)

def update():
    global score
    if keyboard.left:
        bee.x=bee.x-10
    elif keyboard.right:
        bee.x=bee.x+10
    elif keyboard.up:
        bee.y=bee.y-10
    elif keyboard.down:
        bee.y=bee.y+10

    if bee.colliderect(flower):
        score=score+10      
        x1=random.randint(0,500)
        y1=random.randint(0,500)
        flower.pos=x1,y1


def tu():
    global gameover
    gameover=True
    














clock.schedule(tu,20)


pgzrun.go()