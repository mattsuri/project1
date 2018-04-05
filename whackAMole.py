#Matthew Suriawinata
#4/4/18
#whackAMole.py - whack a mole 


from ggame import *

red = Color(0xFF0000, 1) #this is the color red
green = Color(0x00FF00, 1)
blue = Color(0x0000FF, 1)
black = Color(0x000000, 1) 

def mouseClick(event):
    print(event.x)
    print(event.y)
    if event.x < 200 and event.y < 200:
        print("1")
        



    




if __name__ == "__main__":
    blackOutline = LineStyle(1, black)
    
    
    redCircle = CircleAsset(100, blackOutline, red) #radius, outline, fill
    for i in range (0,3):
        height = 50 + i*250
        for i in range (0,3):
            Sprite(redCircle, (20 + i*250, height ))
            
            
    
    App().listenMouseEvent("click", mouseClick)
    App().run() 
