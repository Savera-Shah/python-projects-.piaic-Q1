import random 

def high_low_game():
    num_rounds = 5
    score = 0
    
    print(".....welcome to high_low game.....")
    print("-----------------------------------")
    
    for round in range(1, num_rounds+1):
        
        print(f"round no : {round}")
        user_guess = random.randint(1,100)
        comp_guess = random.randint(1,100)
        
        guess = input("Do you think your number is higher or lower than the computer's? (h/l):   ")
        
        while guess not in ["h" , "l"]:
            guess =input("Please enter either h for higher or l for lower : ")
            
        if (guess == "h" and user_guess> comp_guess)or\
            ( guess =="l" and user_guess<comp_guess):
            print(f"you are right ! the computer no is : {comp_guess}")
            score +=1
        else :
            print(f"Aww, that's incorrect. The computer's number was {comp_guess}")
        print(f"Your score is now {score}\n")
        
    print (f"\n...Thanks for playing ...\n")
    print(f"----------------------------------\n")
    
    if score == num_rounds:
        print (f"Wow! Congratulations, you achieved a perfect score of {score}!\n")
    elif score>= num_rounds//2:
        print(f"Good job! You played well with a score of {score}.\n")
    else:
        print(f"Better luck next time!\n")                        

high_low_game()         
            
        
        
        
    
