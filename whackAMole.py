#Matthew Suriawinata
#4/4/18
#whackAMole.py - whack a mole 


from ggame import *
from random import randint

red = Color(0xFF0000, 1) #this is the color red
green = Color(0x00FF00, 1)
blue = Color(0x0000FF, 1)
black = Color(0x000000, 1) 
white = Color(0xFFFFFF, 1) 


RADIUS = 100 #radius of circles
GAP = 250 #gap distance between circle centers
BORDEREDGE = 50 #border distance
DIAMETER = 200


def moleSpawner():
    num = randint(1,9)
    
    if num == 1:
        data["circle 1"] = True
        
    


def mouseClick(event):
    print(event.x)
    print(event.y)
    
    
        #ROW 1
    if event.y > 50 and event.y < 250 and event.x > 50 and event.x < 250:
        print("CIRCLE", 1)
    if event.y > 50 and event.y < 250 and event.x > 300 and event.x < 500:
        print("CIRCLE", 2)
    if event.y > 50 and event.y < 250 and event.x > 550 and event.x < 750:
        print("CIRCLE", 3) 
        
        
        #ROW 2
    if event.y > 300 and event.y < 500 and event.x > 50 and event.x < 250:
        print("CIRCLE", 4)
    if event.y > 300 and event.y < 500 and event.x > 300 and event.x < 500:
        print("CIRCLE", 5)
    if event.y > 300 and event.y < 500 and event.x > 550 and event.x < 750:
        print("CIRCLE", 6) 
        
        #ROW3
    if event.y > 550 and event.y < 750 and event.x > 50 and event.x < 250:
        print("CIRCLE", 7)
    if event.y > 550 and event.y < 750 and event.x > 300 and event.x < 500:
        print("CIRCLE", 8)
    if event.y > 550 and event.y < 750 and event.x > 550 and event.x < 750:
        print("CIRCLE", 9) 
        
    data["circle 1"] = False
    data["circle 2"] = False
    data["circle 3"] = False
    data["circle 4"] = False
    data["circle 5"] = False
    data["circle 6"] = False
    data["circle 7"] = False
    data["circle 8"] = False    
    data["circle 9"] = False


    




if __name__ == "__main__":
    blackOutline = LineStyle(1, black)
    
    redCircle = CircleAsset(RADIUS, blackOutline, red)
    
    whiteCircle = CircleAsset(RADIUS, blackOutline, white) #radius, outline, fill
    for i in range (0,3):
        height = BORDEREDGE + i*GAP
        for i in range (0,3):
            Sprite(whiteCircle, (BORDEREDGE + i*GAP, height ))
            
            
    
    App().listenMouseEvent("click", mouseClick)
    App().run() 
