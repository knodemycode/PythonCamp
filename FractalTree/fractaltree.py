import turtle

#set up the turtle
wn = turtle.Screen()      # Creates a playground for turtles

alex = turtle.Turtle()    # Create a turtle, assign to alex
alex.speed(11)            # Make alex fast
alex.pu()                 # Pick Up Alex (so he doesn't draw
alex.sety(-200)           # Move him down
alex.left(90)             # Point him up
alex.pd()                 # Put Down Alex




#takes a series of instructions and executes them
#< shrink
#> grow
#F borward
#B back
#R right
#L left
def execute(turt, instructions, angle, distance, ratio):
    
    for i in instructions:
        turt.pensize(distance/10)
        if (i== "<"): #shrink
            distance*= ratio
            
        if (i==">"): #grow
            distance*= 1/ratio
            
        if (i== "F"):#forward
            turt.forward(distance)
            
        if (i=="R"):#right
            turt.right(angle)
            
        if (i=="L"):#left
            turt.left(angle)
            
        if (i=="B"):#back
            turt.backward(distance)


    
#makes a tree
def generateTree(layer, seed="Fb", ruleset=["b","RF<b>BLLF<b>BR"]):
    if (layer == 0):
        return seed
    tree = ""
    for gene in seed:
        if (gene == ruleset[0]):
            tree += ruleset[1]
        else:
            tree += gene
    layer -= 1
    return generateTree(layer, tree, ruleset)


#generates the dragon spiral
def generateSpiral(layer, seed="RF", ruleset=["R","L","L","R"]):
    if (layer == 0):
        return seed
    spiral = ""
    #reverse l and r
    for gene in seed:
        if (gene == ruleset[0]):
            spiral += ruleset[1]
        elif (gene == ruleset[2]):
            spiral += ruleset[3]
        else:
            spiral += gene
    spiral= spiral[::-1]#flipped
    spiral= spiral[1:]+"F"#move Forward command to the end
 
    return generateSpiral(layer-1, seed+"RF"+spiral, ruleset)

print(generateSpiral(3))
execute(alex, generateTree(7), 135, 100, 0.5)#draws a tree
#execute(alex, generateSpiral(8), 85, 10, 1)#draws a dragon spiral

turtle.mainloop()
