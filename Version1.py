# Like and Subscribe! It'd really help the channel!
# Made by Moddo Games
# Current time: 22:33 Seconds

# Import the modules
import tkinter as tk
import random as ra
import time as ti

# Get the window
wn = tk.Tk() # Set the window
wn.title('Cookie Clicker - Moddo Games - 0.0.01') # Set the title

# Setup the window scene (Canvas)
windowWidth = 400
windowHeight = 200
c = tk.Canvas(wn, width=windowWidth, height=windowHeight)
c.pack()

def background(type, res): # 'type' is either vertical or horizontal
    if type == 'v':
        c.create_rectangle(0, 0, windowWidth+5, windowHeight+5, fill='lightblue') # Create the main background
        
        # Create the stripes
        spawnX1, spawnY1 = 0, 0
        spawnX2, spawnY2 = 25, windowHeight+5
        
        changeAmount = spawnX2 + 20
        for VBackground in range(res):
            c.create_rectangle(spawnX1, spawnY1, spawnX2, spawnY2, fill='purple') # Make the stripes
            
            spawnX1 += changeAmount
            spawnX2 += changeAmount
    elif type == 'h':
        pass # like and subscribe to see more!

background('v', 25) # can change when settings are made

# Make the cookie
def cookie():
    backgroundCookie = c.create_oval(25, 50, 175, 185, fill='#EECC77')
    
    for chip in range(ra.randint(1, 15)):
        minX, minY = 35, 50
        maxX, maxY = 165, 175
        
        positionX = ra.randint(minX, maxX)
        positionY = ra.randint(minY, maxY)
        
        size = ra.randint(5, 15)
        c.create_oval(positionX, positionY, positionX+size, positionY+size, fill='#7B3D11') # Let's make it clickable next episode! Like and subscribe for more content like this, and to support the channel!
    
cookie()

# Ensure the window stays open, and on top
wn.attributes("-topmost", True)
wn.mainloop()

# Todo Section - Will expand
# TODO: Make Settings