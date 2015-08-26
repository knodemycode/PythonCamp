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


#Tkinter._test()
#if that didn't work do tkinter._test() -- python 3


starFiles = ("bluestar.gif","greenstar.gif","silverstar.gif","goldstar.gif","whitestar.gif")
def starPicker(num):
    root = Tk()
    root.title("YourStar")
    photo = PhotoImage(file=starFiles[num])
    w = Label(image=photo)
    w.photo = photo
    w.pack()
    root.mainloop()
        
 
def main():
    """
    http://www.tkdocs.com/tutorial/firstexample.html
    """

    #ask the user what their age is (print)
    #collect the value of their age (input)

    #add a series of conditionals here
    #to call starPicker with a series of values
    #if the age is less than 15, the number is 0
    #if the age is less than 30, the number is 1
    #if the age is less than 45, the number is 2
    #if the age is less than 60, the number is 3
    #else, the number is 4
    
    starPicker(4)


	

main()

