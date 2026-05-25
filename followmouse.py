import pgzrun,random

WIDTH=900
HEIGHT=900

mango=Actor("goo")

def draw():
    screen.fill((33,44,55))
    mango.draw()
    mes=("Guess where the boundaries are. I can't go further")
    screen.draw.text(mes, center=(450,450),fontsize=30)

    r=random.randint(0,255)
    b=random.randint(0,255)
    g=random.randint(0,255)
    rec=Rect((100,100),(300,300))
    screen.draw.rect(rec,(r,b,255))

def on_mouse_down(pos):
    x=pos[0]
    y=pos[1]

    if x>=400:
        x=100
    elif x<100:
        x=125
    if y>400:
        y=366.5
    elif y<100:
        y=133.5

    mango.x=x
    mango.y=y

















pgzrun.go()