"""
The tkdocs tutorial
http://www.tkdocs.com/tutorial/firstexample.html
"""
import pygame
from Tkinter import *
#if this doesn't work import _tkinter  (for python 3)
"""
http://tkinter.unpythonic.net/wiki/How_to_install_Tkinter
"""
import ttk
#in python 3 you need to from tkinter import ttk



def add(a, b):
    answer = 0
    return answer
        

def subtract(a, b):
    answer = 0
    return answer
    #return the value of b subtracted from a


def multiply(a, b):
    answer = 0
    return answer
    #return the value of a multiplied by b

def divide(a, b):
    answer = 0
    return answer
    #return the value of a divided by b


def main():
    """
    http://www.tkdocs.com/tutorial/firstexample.html
    """
    #the main window
    
    root = Tk()
    root.title("Calculator Window")

    #the main frame
    mframe = ttk.Frame(root, padding="3 3 12 12")
    mframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mframe.columnconfigure(0, weight=1)
    mframe.rowconfigure(0, weight=1)

    #important variables
    aInput = StringVar()
    aInput.set("0")
    bInput = StringVar()
    bInput.set("0")
    oput = StringVar()


    
    #fields for entering numbers
    mput_entry = ttk.Entry(mframe, width=7, textvariable = aInput)
    mput_entry.grid(column=1, row=2, sticky=(W, E))
    mput_entry2 = ttk.Entry(mframe, width=7, textvariable = bInput)
    mput_entry2.grid(column=2, row=2, sticky=(W, E))

    #label to see the output
    ttk.Label(mframe, textvariable=oput).grid(column=3, row=2, sticky=(W,E))
    
    
    #buttons for actions
    ttk.Button(mframe, text="+", command=lambda: oput.set(add(float(aInput.get()), float(bInput.get())))).grid(column=1, row=3, sticky=W)
    ttk.Button(mframe, text="-", command=lambda: oput.set(subtract(float(aInput.get()), float(bInput.get())))).grid(column=2, row=3, sticky=W)
    ttk.Button(mframe, text="*", command=lambda: oput.set(multiply(float(aInput.get()), float(bInput.get())))).grid(column=3, row=3, sticky=W)
    ttk.Button(mframe, text="/", command=lambda: oput.set(divide(float(aInput.get()), float(bInput.get())))).grid(column=4, row=3, sticky=W)

    #put things on there in a grid
    ttk.Label(mframe, text="a").grid(column=1, row=1, sticky=W)
    ttk.Label(mframe, text="b").grid(column=2, row=1, sticky=W)
    ttk.Label(mframe, text="result").grid(column=3, row=1, sticky=W)

    #add a little padding to each child
    for child in mframe.winfo_children(): child.grid_configure(padx=5, pady=5)
    
    #put focus on the entry widget (where they type things)
    mput_entry.focus()
    #if they press Return in the window, it should run the function as if they pressed the button
    #root.bind('<Return>', myfunc)

    #make it all run
    root.mainloop()



main()

