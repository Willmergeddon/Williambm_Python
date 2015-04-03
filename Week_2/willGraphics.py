from graphics import *
import random

#Window and variable initialisation

window = GraphWin("Visualisation", 800, 800)
firPart = None
secPart = None
counter = 0 # counter for possible limiting

#Loop that creates shapes

while True:
    
    
# Read in the data in the data file
    datafile = open("data.txt",'r')
    
    
    for line in datafile:
        number = float(line)
        firPart = int(number*6)
        secPart = int(str(number*8).split('.')[1])
        
        #test variables
        #print(str(firPart) + " " + str(secPart))
        #posX= random.randint(0,100)
    
    #Storing variables into other variables for any adjusting
    
        posR= random.randint(15,20)
        posX= firPart
        posY= secPart
        posZ= secPart
        
    #creating circles based on variables, including colour
    
        sp2 = Circle(Point(posX,posX),posZ+(posX/2))
        sp2.setWidth(posR)
        sp2.draw(window)
        sp2.setOutline(color_rgb(posX/6,posY/6,posZ))
        
        #loop 'ends' here
       
        
        
        
         
        
            
            




# Waits until the mouse is clicked before closing the window
window.getMouse()