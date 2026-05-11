import pgzrun, random
WIDTH=500
HEIGHT=500
def draw():
    x=300
    y=300
    for i in range(300):
        x=x-1
        y=y-1
        r=random.randint(0,255)
        b=random.randint(0,255)
        g=random.randint(0,255)
        rec=Rect((250,250),(x,y))
        rec.center=250,250
        screen.draw.filled_rect(rec,(0,0,g))















pgzrun.go()