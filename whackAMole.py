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
DIAMETER = 200



def mouseClick(event):
    print(event.x)
    print(event.y)
    
    
        #ROW 1
    if event.y > (BORDEREDGE*1 + DIAMETER*(0) and event.y < (BORDEREDGE*1 + DIAMETER*1) and event.x > (BORDEREDGE*1 + DIAMETER*(0)) and event.x < (BORDEREDGE*1 + DIAMETER*1)):
        print("CIRCLE", 1)
    if event.y > (BORDEREDGE*1 + DIAMETER*(0) and event.y < (BORDEREDGE*1 + DIAMETER*1) and event.x > (BORDEREDGE*2 + DIAMETER*(1)) and event.x < (BORDEREDGE*2 + DIAMETER*2)):
        print("CIRCLE", 2)
    if event.y > (BORDEREDGE*1 + DIAMETER*(0) and event.y < (BORDEREDGE*1 + DIAMETER*1) and event.x > (BORDEREDGE*3 + DIAMETER*(2)) and event.x < (BORDEREDGE*3 + DIAMETER*3)):
        print("CIRCLE", 3) 
        
        
        #ROW 2
    if event.y > (BORDEREDGE*2 + DIAMETER*(1) and event.y < (BORDEREDGE*2 + DIAMETER*2) and event.x > (BORDEREDGE*1 + DIAMETER*(0)) and event.x < (BORDEREDGE*1 + DIAMETER*1)):
        print("CIRCLE", 4)
    if event.y > (BORDEREDGE*2 + DIAMETER*(1) and event.y < (BORDEREDGE*2 + DIAMETER*2) and event.x > (BORDEREDGE*2 + DIAMETER*(1)) and event.x < (BORDEREDGE*2 + DIAMETER*2)):
        print("CIRCLE", 5)
    if event.y > (BORDEREDGE*2 + DIAMETER*(1) and event.y < (BORDEREDGE*2 + DIAMETER*2) and event.x > (BORDEREDGE*3 + DIAMETER*(2)) and event.x < (BORDEREDGE*3 + DIAMETER*3)):
        print("CIRCLE", 6)
        
        #ROW3
    if event.y > (BORDEREDGE*3 + DIAMETER*(2) and event.y < (BORDEREDGE*3 + DIAMETER*3) and event.x > (BORDEREDGE*1 + DIAMETER*(0)) and event.x < (BORDEREDGE*1 + DIAMETER*1)):
        print("CIRCLE", 7)
    if event.y > (BORDEREDGE*3 + DIAMETER*(2) and event.y < (BORDEREDGE*3 + DIAMETER*3) and event.x > (BORDEREDGE*2 + DIAMETER*(1)) and event.x < (BORDEREDGE*2 + DIAMETER*2)):
        print("CIRCLE", 8)
    if event.y > (BORDEREDGE*3 + DIAMETER*(2) and event.y < (BORDEREDGE*3 + DIAMETER*3) and event.x > (BORDEREDGE*3 + DIAMETER*(2)) and event.x < (BORDEREDGE*3 + DIAMETER*3)):
        print("CIRCLE", 9)
    
        



    




if __name__ == "__main__":
    blackOutline = LineStyle(1, black)
    
    
    redCircle = CircleAsset(RADIUS, blackOutline, red) #radius, outline, fill
    for i in range (0,3):
        height = BORDEREDGE + i*GAP
        for i in range (0,3):
            Sprite(redCircle, (BORDEREDGE + i*GAP, height ))
            
            
    
    App().listenMouseEvent("click", mouseClick)
    App().run() 
