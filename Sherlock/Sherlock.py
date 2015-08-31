"""
The tkdocs tutorial
http://www.tkdocs.com/tutorial/firstexample.html
"""
import pygame
import time
from Tkinter import *
#if this doesn't work import _tkinter  (for python 3)
"""
http://tkinter.unpythonic.net/wiki/How_to_install_Tkinter
"""
import ttk
#in python 3 you need to from tkinter import ttk


#Tkinter._test()
#if that didn't work do tkinter._test() -- python 3

IMAGES= ("milk.gif","hole.gif","footprint.gif","hair.gif","fox.gif")

def play(image):
    i = 0
    while(True):
        time.sleep(0.2)
        image.photo = PhotoImage(file = IMAGES[i%len(IMAGES)])
        i = i+1
        root.mainloop()

        
def main():
    root = Tk()
    root.title("sherlock")

    #the main frame
    mframe = ttk.Frame(root, padding="3 3 12 12")
    mframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mframe.columnconfigure(0, weight=1)
    mframe.rowconfigure(0, weight=1)

    #the Sorting Hat image
    photo = PhotoImage(file=IMAGES[0])
    image = ttk.Label(mframe, image=photo)
    image.photo = photo
    image.grid(column = 2, row = 1, sticky = N)
    
    for child in mframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    ttk.Button(mframe, text="play", command=lambda: play(image)).grid(column = 1, row = 1, sticky = N)

    
    
    root.mainloop()
    print("after mainloop")
    


	

main()

