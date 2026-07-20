import pgzrun,os
os.environ["SDL_VIDEO_CENTERED"]="1"

WIDTH=1000
HEIGHT=800



answer1=Rect(50,350,425,200)
answer2=Rect(550,350,425,200)
answer3=Rect(50,575,425,200)
answer4=Rect(550,575,425,200)
question=Rect(50,25,700,100)

def draw():
    screen.fill((100,100,100))
    screen.draw.filled_rect(answer1,(244,45,54))
    screen.draw.filled_rect(answer2,(144,98,165))
    screen.draw.filled_rect(answer3,(10,201,165))
    screen.draw.filled_rect(answer4,(234,43,165))
    screen.draw.filled_rect(question,(255,60,255))













































































































pgzrun.go()