import pgzrun, random
start=0
finish=8
satt=[]

run=True
        

def draw():
 global run
 if run==True:
    for i in range(8):
        sat=Actor("sat")
        x=random.randint(0,500)
        y=random.randint(0,500)
        sat.x=x
        sat.y=y
        sat.draw()
        satt.append(sat)
        screen.draw.text(str(i+1),center=((x-20),(y+20)),fontsize=20)
    run=False


def on_mouse_down(pos):
    global start
    if satt[start].collidepoint(pos):
        x=satt[start].x
        y=satt[start].y


        

    















pgzrun.go()