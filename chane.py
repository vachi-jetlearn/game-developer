import pgzrun
click=True


WIDTH=500
HEIGHT=500

c1=Actor("goosy")

def draw():
    screen.fill((0,0,0))
    if click==True:
            c1.image=("eva")
            
    else:
        c1.image=("goosy")
    c1.draw()
        

       
   
def on_mouse_down(pos):
    global click
    if c1.image==("goosy"):
        click=True
    else:
        click=False

    
    
    x=pos[0]
    y=pos[1]

    c1.x=x
    c1.y=y
    
pgzrun.go()
