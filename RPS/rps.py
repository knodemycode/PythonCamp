import random

again = "y"
while(again == "y"):
    user = raw_input("rock, paper, or scissors?")

    #student RPS
    computer = random.randint(0,2)
    if computer == 0:
        computer = "rock"
    if computer == 1:
        computer = "paper"
    if computer == 2:
        computer = "scissors"
                    

    print("Computer choice: " + computer)
    if (user == computer):
        print("Draw! You picked the same things")
    elif(user == "rock"):
        if(computer =="paper"):
            print("Paper covers rock, Computer wins.")
        if(computer =="scissors"):
            print("Rock smashes scissors. User wins.")
    elif(user == "paper"):
        if(computer =="scissors"):
            print("Scissors cut paper. Computer wins")
        if(computer == "rock"):
            print("Rock covers paper. User wins.")
    elif(user == "scissors"):
        if(computer == "paper"):
            print("Scissors cut paper. Computer wins.")
        if(computer == "rock"):
            print("Rock smashes scissors. User  wins.")
    else:
        print("not a valid choice.")

    again = raw_input("Play again? y/n ")
        
