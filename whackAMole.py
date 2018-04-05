#Matthew Suriawinata
#4/4/18
#whackAMole.py - whack a mole 


from ggame import *

red = Color(0xFF0000, 1) #this is the color red
green = Color(0x00FF00, 1)
blue = Color(0x0000FF, 1)
black = Color(0x000000, 1) 




    



if __name__ == "__main__":
    blackOutline = LineStyle(1, black)
    
    
    redCircle = CircleAsset(50, blackOutline, red) #radius, outline, fill
    for i in range (0,5):
        height = 50 + i*150
        for i in range (0,5):
            Sprite(redCircle, (20 + i*150, height ))
    
    App().run() 