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


class Hat:
    def __init__(self):
        #declare variables
        self.qa = 0 #questions answered
        self.questions = ("are you brave?", "are you cunning?", "are you smart?")
        self.answers = []

    def yesPressed(self, oput):
        self.qa = self.qa + 1
        self.answers.append("yes")
        self.nextQuestion(oput)

    def noPressed(self, oput):
        self.qa = self.qa + 1
        self.answers.append("no")
        self.nextQuestion(oput)

    def nextQuestion(self, oput):

        if (self.qa <len(self.questions)):
            oput.set( self.questions[self.qa])
        else:
            oput.set( self.sort() )


    def sort(self):
        answer1 = self.answers[0]
        answer2 = self.answers[1]
        answer3 = self.answers[2]
        
        """depending on the questions and answers
        return Slytherin, Gryffindor, Ravenclaw, or Hufflepuff
        """
        
        
def main():
    root = Tk()
    root.title("Sorting Hat")

    #the main frame
    mframe = ttk.Frame(root, padding="3 3 12 12")
    mframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mframe.columnconfigure(0, weight=1)
    mframe.rowconfigure(0, weight=1)

    #the Sorting Hat image
    photo = PhotoImage(file="Hat.gif")
    hat = ttk.Label(mframe, image=photo)#.grid(column = 1, row = 1, sticky = N)
    hat.photo = photo
    hat.grid(column = 1, row = 1, sticky = N)

    sortingHat = Hat()

    #yes/no buttons
    yesBtn = ttk.Button(mframe, text="a) yes", command=lambda: sortingHat.yesPressed(oput))
    yesBtn.grid(column = 1, row = 3, sticky = W)

    noBtn = ttk.Button(mframe, text="a) no", command=lambda: sortingHat.noPressed(oput))
    noBtn.grid(column = 2, row = 3, sticky = W)

    #question
    oput = StringVar()
    oput.set(sortingHat.questions[0])
    ttk.Label(mframe, textvariable=oput).grid(column = 1, row = 2, sticky = W)


    for child in mframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    
    
    root.mainloop()

    


	

main()

