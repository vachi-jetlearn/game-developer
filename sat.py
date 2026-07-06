import pgzrun, random
start=0
finish=8
satt=[]
lines=[]
WIDTH=900
HEIGHT=900

for i in range(8):
    sat=Actor("sat")
    x=random.randint(100,500)
    y=random.randint(100,500)
    satt.append(sat)
    sat.x=x
    sat.y=y


run=True

        

def draw():

    i=0
    for sat in satt:
        sat.draw()
        x=sat.pos[0]
        y=sat.pos[1]
        screen.draw.text(str(i+1),center=((x-20),(y+20)),fontsize=20)
        i=i+1

    for i in lines:
       screen.draw.line(i[0],i[1],(255,255,255))

    


def on_mouse_down(pos):
    global lines
    global start
    if start<finish:
        if satt[start].collidepoint(pos):
            if start>0:
                lines.append((satt[start-1].pos, satt[start].pos))
            start=start+1
        else:
            lines=[]
            start=0
                

        

    















pgzrun.go()