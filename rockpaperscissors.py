import random

Strings = ["Rock", "Paper", "Scissor"]

print("Your Options are ", Strings)

while(1==1):
    
    human = input(f"Enter your move or to quit enter (exit): ")
    
    robot = random.choice(Strings)
    
    print(f"robot move is {robot}")
    
    if(human == "exit"):
        
        print("Thanks for playing!!!")
        
        break
    
    elif(human == robot):
        
        print("Match have drawn")
    
    elif((human == "Rock" and robot == "Scissor") or (human == "Scissor" and robot == "Paper") or (human == "Paper" and robot == "Rock")):
        
        print("You have won!!!")
    
    elif((robot == "Rock" and human == "Scissor") or (robot == "Scissor" and human == "Paper") or (robot == "Paper" and human == "Rock")):
        
        print("You have lost!!!")
                
    else:
        
        print("Please ensure that you have entered correctly")
        
else:
    
    print("Not verified")