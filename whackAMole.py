#Matthew Suriawinata
#4/4/18
#whackAMole.py - whack a mole 


from ggame import *

red = Color(0xFF0000, 1) #this is the color red
green = Color(0x00FF00, 1)
blue = Color(0x0000FF, 1)
black = Color(0x000000, 1) 

RADIUS = 100 #radius of circles
GAP = 250 #gap distance between circle centers
BORDEREDGE = 50 #border distance
DIAMETER = RADIUS * 2



def mouseClick(event):
    print(event.x)
    print(event.y)
    for i in range(1,4):
        if event.y > (BORDEREDGE*i + DIAMETER*(i-1) and event.y < (BORDEREDGE*i + DIAMETER*i)):
            x
            for i in range(1,4):
                if event.x > (BORDEREDGE*i + DIAMETER*(i-1)) and event.x < (BORDEREDGE*i + DIAMETER*i):
                    print("CIRCLE", str(0+i))
        



    




if __name__ == "__main__":
    blackOutline = LineStyle(1, black)
    
    
    redCircle = CircleAsset(RADIUS, blackOutline, red) #radius, outline, fill
    for i in range (0,3):
        height = BORDEREDGE + i*GAP
        for i in range (0,3):
            Sprite(redCircle, (BORDEREDGE + i*GAP, height ))
            
            
    
    App().listenMouseEvent("click", mouseClick)
    App().run() 
