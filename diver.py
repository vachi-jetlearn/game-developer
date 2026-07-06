import pgzrun, random, time

WIDTH=1200
HEIGHT=673

i=True

diver=Actor("diver")
pearl=Actor("pearl")

def draw():
    screen.blit("oc",(0,0))

    diver.draw()
    
    if pearl.visible:
        pearl.draw()

    
    


    
def update():

    if keyboard.left:
        diver.x-=5

    if keyboard.right:
     diver.x+=5

    if keyboard.up:
        diver.y-=5
    
    if keyboard.down:
        diver.y+=5

    if diver.colliderect(pearl):
       

        pearl.visible=False
        time.sleep(10)
        
        loca()


def loca():
    x=random.randint(100,1100)
    y=random.randint(50,630)

    pearl.pos=x,y
    
    pearl.visible=True

pgzrun.go()